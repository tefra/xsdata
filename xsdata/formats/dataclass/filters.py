import math
import textwrap
from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from decimal import Decimal
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Type
from xml.etree.ElementTree import QName
from xml.sax.saxutils import quoteattr

from docformatter import format_code
from jinja2 import Environment

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrChoice
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.formats.converter import converter
from xsdata.formats.dataclass import utils
from xsdata.models.config import DocstringStyle
from xsdata.models.config import GeneratorAlias
from xsdata.models.config import GeneratorConfig
from xsdata.utils import text
from xsdata.utils.collections import unique_sequence
from xsdata.utils.namespaces import clean_uri

CLASS = 0
FIELD = 1
MODULE = 2
PACKAGE = 3


@dataclass
class Filters:

    class_aliases: Dict = field(default_factory=dict)
    field_aliases: Dict = field(default_factory=dict)
    package_aliases: Dict = field(default_factory=dict)
    module_aliases: Dict = field(default_factory=dict)

    class_case: Callable = field(default=text.pascal_case)
    field_case: Callable = field(default=text.snake_case)
    package_case: Callable = field(default=text.snake_case)
    module_case: Callable = field(default=text.snake_case)

    class_safe_prefix: str = field(default="type")
    field_safe_prefix: str = field(default="value")
    package_safe_prefix: str = field(default="pkg")
    module_safe_prefix: str = field(default="mod")

    docstring_style: DocstringStyle = field(default=DocstringStyle.RST)
    max_line_length: int = field(default=79)

    cache: Dict = field(default_factory=lambda: defaultdict(dict), init=False)

    def register(self, env: Environment):
        env.filters.update(
            {
                "field_name": self.field_name,
                "field_default": self.field_default_value,
                "field_metadata": self.field_metadata,
                "field_type": self.field_type,
                "class_name": self.class_name,
                "class_params": self.class_params,
                "format_string": self.format_string,
                "format_docstring": self.format_docstring,
                "constant_name": self.constant_name,
                "constant_value": self.constant_value,
                "default_imports": self.default_imports,
                "format_metadata": self.format_metadata,
                "type_name": self.type_name,
                "text_wrap": self.text_wrap,
                "text_strip": self.text_strip,
            }
        )

    def class_name(self, name: str) -> str:
        """Convert the given string to a class name according to the selected
        conventions or use an existing alias."""
        cache = self.cache[CLASS]
        if name not in cache:
            cache[name] = self.class_aliases.get(name) or self._class_name(name)

        return cache[name]

    def class_params(self, obj: Class):
        is_enum = obj.is_enumeration
        for attr in obj.attrs:
            name = attr.name
            result = self.constant_name(name) if is_enum else self.field_name(name)
            yield result, (attr.help or "").strip()

    def _class_name(self, name: str) -> str:
        return self.class_case(utils.safe_snake(name, self.class_safe_prefix))

    def field_name(self, name: str) -> str:
        """Convert the given string to a field name according to the selected
        conventions or use an existing alias."""
        cache = self.cache[FIELD]
        if name not in cache:
            cache[name] = self.field_aliases.get(name) or self._attribute_name(name)

        return cache[name]

    def _attribute_name(self, name: str) -> str:
        return self.field_case(utils.safe_snake(name, self.field_safe_prefix))

    def constant_name(self, name: str) -> str:
        """Apply python conventions for constant names."""
        return self.field_name(name).upper()

    def module_name(self, name: str) -> str:
        """Convert the given string to a module name according to the selected
        conventions or use an existing alias."""
        cache = self.cache[MODULE]
        if name not in cache:
            cache[name] = self.module_aliases.get(name) or self._module_name(name)

        return cache[name]

    def _module_name(self, name: str) -> str:
        return self.module_case(
            utils.safe_snake(clean_uri(name), self.module_safe_prefix)
        )

    def package_name(self, name: str) -> str:
        """Convert the given string to a package name according to the selected
        conventions or use an existing alias."""
        cache = self.cache[PACKAGE]
        if name not in cache:

            if name in self.package_aliases:
                cache[name] = self.package_aliases[name]
            else:
                cache[name] = ".".join(
                    self.package_aliases.get(part) or self._package_name(part)
                    for part in name.split(".")
                )

        return cache[name]

    def _package_name(self, part: str) -> str:
        return self.package_case(utils.safe_snake(part, self.package_safe_prefix))

    def type_name(self, attr_type: AttrType) -> str:
        """Return native python type name or apply class name conventions."""
        return attr_type.native_name or self.class_name(attr_type.name)

    def field_metadata(
        self, attr: Attr, parent_namespace: Optional[str], parents: List[str]
    ) -> Dict:
        """Return a metadata dictionary for the given attribute."""

        name = namespace = None

        if not attr.is_nameless and attr.local_name != self.field_name(attr.name):
            name = attr.local_name

        if parent_namespace != attr.namespace or attr.is_attribute:
            namespace = attr.namespace

        types = list({x.native_type for x in attr.types if x.native})
        restrictions = attr.restrictions.asdict(types)
        doc = attr.help if self.docstring_style == DocstringStyle.ACCESSIBLE else None

        return self.filter_metadata(
            {
                "name": name,
                "type": attr.xml_type,
                "namespace": namespace,
                "mixed": attr.mixed,
                "choices": self.field_choices(attr, parent_namespace, parents),
                **restrictions,
                "doc": doc,
            }
        )

    def field_choices(
        self, attr: Attr, parent_namespace: Optional[str], parents: List[str]
    ) -> Optional[List]:
        """
        Return a list of metadata dictionaries for the choices of the given
        attribute.

        Return None if attribute has no choices.
        """

        if not attr.choices:
            return None

        def build(choice: AttrChoice) -> Dict:
            types = list({x.native_type for x in choice.types if x.native})
            restrictions = choice.restrictions.asdict(types)
            namespace = (
                choice.namespace if parent_namespace != choice.namespace else None
            )

            return self.filter_metadata(
                {
                    "name": choice.name,
                    "wildcard": choice.is_wildcard,
                    "type": self.choice_type(choice, parents),
                    "namespace": namespace,
                    **restrictions,
                }
            )

        return list(map(build, attr.choices))

    @classmethod
    def filter_metadata(cls, data: Dict) -> Dict:
        return {
            key: value
            for key, value in data.items()
            if value is not None and value is not False
        }

    def format_metadata(self, data: Any, indent: int = 0, key: str = "") -> str:
        """Prettify field metadata for code generation."""

        if isinstance(data, dict):
            return self.format_dict(data, indent)

        if isinstance(data, (list, tuple)):
            return self.format_iterable(data, indent)

        if isinstance(data, str):
            return self.format_string(data, indent, key, 4)

        return str(data)

    def format_dict(self, data: Dict, indent: int) -> str:
        """Return a pretty string representation of a dict."""
        ind = " " * indent
        fmt = '    {}"{}": {},'
        lines = [
            fmt.format(ind, key, self.format_metadata(value, indent + 4, key))
            for key, value in data.items()
        ]

        return "{{\n{}\n{}}}".format("\n".join(lines), ind)

    def format_iterable(self, data: Iterable, indent: int) -> str:
        """Return a pretty string representation of an iterable."""
        ind = " " * indent
        fmt = "    {}{},"
        lines = [
            fmt.format(ind, self.format_metadata(value, indent + 4)) for value in data
        ]
        return "(\n{}\n{})".format("\n".join(lines), ind)

    def format_string(self, data: str, indent: int, key: str = "", pad: int = 0) -> str:
        """
        Return a pretty string representation of a string.

        If the total length of the input string plus indent plus the key
        length and the additional pad is more than the max line length,
        wrap the text into multiple lines, avoiding breaking long words
        """
        if data.startswith("Type[") and data.endswith("]"):
            return data if data[5] == '"' else data[5:-1]

        if key == "pattern":
            return f'r"{data}"'

        if data == "":
            return '""'

        start = indent + 2  # plus quotes
        start += len(key) + pad if key else 0

        value = text.escape_string(data)
        length = len(value) + start
        if length < self.max_line_length or " " not in value:
            return f'"{value}"'

        next_indent = indent + 4
        value = "\n".join(
            [
                f'{" " * next_indent}"{line}"'
                for line in textwrap.wrap(
                    value,
                    width=self.max_line_length - next_indent - 2,  # plus quotes
                    drop_whitespace=False,
                    replace_whitespace=False,
                    break_long_words=True,
                )
            ]
        )
        return f"(\n{value}\n{' ' * indent})"

    def text_wrap(self, string: str, offset: int = 0) -> str:
        """Wrap text in respect to the max line length and the given offset."""
        return "\n".join(
            textwrap.wrap(
                string,
                width=self.max_line_length - offset,
                drop_whitespace=True,
                replace_whitespace=True,
                break_long_words=False,
                subsequent_indent="    ",
            )
        )

    @classmethod
    def text_strip(cls, string: Optional[str]) -> str:
        """Remove all whitespace from every line of the string."""
        if not string:
            return ""

        return "\n".join(map(str.strip, string.splitlines()))

    def format_docstring(self, doc_string: str, level: int) -> str:
        """Format doc strings."""

        content, params = doc_string.rsplit('"""', 1)

        params = params.strip()

        if content.strip() == '"""' and not params:
            return ""

        content += ' """' if content.endswith('"') else '"""'

        max_length = self.max_line_length - level * 4
        content = format_code(
            content,
            summary_wrap_length=max_length,
            description_wrap_length=max_length - 7,
            make_summary_multi_line=True,
        )

        if params:
            content = content.rstrip('"""').strip()
            new_lines = "\n" if content.endswith('"""') else "\n\n"
            content += f'{new_lines}{params}\n"""'

        return content

    def field_default_value(self, attr: Attr, ns_map: Optional[Dict] = None) -> Any:
        """Generate the field default value/factory for the given attribute."""
        if attr.is_list or (attr.is_tokens and not attr.default):
            return "list"
        if attr.is_dict:
            return "dict"
        if not isinstance(attr.default, str):
            return attr.default
        if attr.default.startswith("@enum@"):
            return self.field_default_enum(attr)

        types = converter.sort_types(
            list(
                {attr_type.native_type for attr_type in attr.types if attr_type.native}
            )
        )

        if attr.is_tokens:
            return self.field_default_tokens(attr, types)

        return self.prepare_default_value(
            converter.deserialize(attr.default, types, ns_map=ns_map)
        )

    def field_default_enum(self, attr: Attr) -> str:
        source, enumeration = attr.default[6:].split("::", 1)
        source = next(x.alias or source for x in attr.types if x.name == source)
        return f"{self.class_name(source)}.{self.constant_name(enumeration)}"

    def field_default_tokens(self, attr: Attr, types: List[Type]) -> str:
        assert isinstance(attr.default, str)

        tokens = ", ".join(
            str(self.prepare_default_value(converter.deserialize(val, types)))
            for val in attr.default.split()
        )
        return f"lambda: [{tokens}]"

    def field_type(self, attr: Attr, parents: List[str]) -> str:
        """Generate type hints for the given attribute."""

        type_names = unique_sequence(
            self.field_type_name(x, parents) for x in attr.types
        )

        result = ", ".join(type_names)
        if len(type_names) > 1:
            result = f"Union[{result}]"

        if attr.is_tokens:
            result = f"List[{result}]"

        if attr.is_list:
            result = f"List[{result}]"
        elif attr.is_dict:
            result = "Dict"
        elif attr.default is None and not attr.is_factory:
            result = f"Optional[{result}]"

        return result

    def choice_type(self, choice: AttrChoice, parents: List[str]) -> str:
        """
        Generate type hints for the given choice.

        Choices support a subset of features from normal attributes.
        First of all we don't have a proper type hint but a type
        metadata key. That's why we always need to wrap as Type[xxx].
        The second big difference is that our choice belongs to a
        compound field that might be a list, that's why list restriction
        is also ignored.
        """
        type_names = unique_sequence(
            self.field_type_name(x, parents) for x in choice.types
        )

        result = ", ".join(type_names)
        if len(type_names) > 1:
            result = f"Union[{result}]"

        if choice.is_tokens:
            result = f"List[{result}]"

        return f"Type[{result}]"

    def field_type_name(self, attr_type: AttrType, parents: List[str]) -> str:
        name = (
            self.class_name(attr_type.alias)
            if attr_type.alias
            else self.type_name(attr_type)
        )

        if attr_type.forward and attr_type.circular:
            outer_str = ".".join(map(self.class_name, parents))
            name = f'"{outer_str}"'
        elif attr_type.forward:
            outer_str = ".".join(map(self.class_name, parents))
            name = f'"{outer_str}.{name}"'
        elif attr_type.circular:
            name = f'"{name}"'

        return name

    def constant_value(self, attr: Attr) -> str:
        """Return the attr default value or type as constant value."""
        attr_type = attr.types[0]
        if attr_type.native:
            return f'"{attr.default}"'

        if attr_type.alias:
            return self.class_name(attr_type.alias)

        return self.type_name(attr_type)

    @classmethod
    def prepare_default_value(cls, value: Any) -> Any:
        if isinstance(value, str):
            return quoteattr(value)

        if isinstance(value, float):
            return f"float('{value}')" if math.isinf(value) else value

        if isinstance(value, Decimal):
            return repr(value)

        if isinstance(value, QName):
            return f'QName("{value.text}")'

        return value

    @classmethod
    def type_is_included(cls, output: str, type_name: str) -> bool:
        return (
            f": {type_name}" in output
            or f"[{type_name}" in output
            or f", {type_name}" in output
            or f"= {type_name}" in output
        )

    @classmethod
    def default_imports(cls, output: str) -> str:
        """Generate the default imports for the given package output."""
        result = []

        dataclasses = []
        if "@dataclass" in output:
            dataclasses.append("dataclass")
        if "field(" in output:
            dataclasses.append("field")

        if dataclasses:
            result.append(f"from dataclasses import {', '.join(dataclasses)}")

        if cls.type_is_included(output, "Decimal"):
            result.append("from decimal import Decimal")

        if "(Enum)" in output:
            result.append("from enum import Enum")

        typing_patterns = {
            "Dict": [": Dict"],
            "List": [": List["],
            "Optional": ["Optional["],
            "Type": ["Type["],
            "Union": ["Union["],
        }

        types = [
            name
            for name, patterns in typing_patterns.items()
            if any(pattern in output for pattern in patterns)
        ]
        if types:
            result.append(f"from typing import {', '.join(types)}")

        if cls.type_is_included(output, "QName"):
            result.append("from xml.etree.ElementTree import QName")

        return "\n".join(result)

    @classmethod
    def from_config(cls, config: GeneratorConfig) -> "Filters":
        def index_aliases(aliases: List[GeneratorAlias]) -> Dict:
            return {alias.source: alias.target for alias in aliases}

        return cls(
            class_aliases=index_aliases(config.aliases.class_name),
            field_aliases=index_aliases(config.aliases.field_name),
            package_aliases=index_aliases(config.aliases.package_name),
            module_aliases=index_aliases(config.aliases.module_name),
            class_case=config.conventions.class_name.case.func,
            field_case=config.conventions.field_name.case.func,
            package_case=config.conventions.package_name.case.func,
            module_case=config.conventions.module_name.case.func,
            class_safe_prefix=config.conventions.class_name.safe_prefix,
            field_safe_prefix=config.conventions.field_name.safe_prefix,
            package_safe_prefix=config.conventions.package_name.safe_prefix,
            module_safe_prefix=config.conventions.module_name.safe_prefix,
            docstring_style=config.output.docstring_style,
            max_line_length=config.output.max_line_length,
        )
