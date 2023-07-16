import re
import sys
import textwrap
from collections import defaultdict
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type

from docformatter import configuration
from docformatter import format
from jinja2 import Environment

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.config import DocstringStyle
from xsdata.models.config import ExtensionType
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import GeneratorExtension
from xsdata.models.config import ObjectType
from xsdata.models.config import OutputFormat
from xsdata.utils import collections
from xsdata.utils import namespaces
from xsdata.utils import text
from xsdata.utils.objects import literal_value


class Filters:
    DEFAULT_KEY = "default"
    FACTORY_KEY = "default_factory"
    UNESCAPED_DBL_QUOTE_REGEX = re.compile(r"([^\\])\"")

    __slots__ = (
        "substitutions",
        "extensions",
        "class_case",
        "field_case",
        "constant_case",
        "package_case",
        "module_case",
        "class_safe_prefix",
        "field_safe_prefix",
        "constant_safe_prefix",
        "package_safe_prefix",
        "module_safe_prefix",
        "docstring_style",
        "max_line_length",
        "union_type",
        "subscriptable_types",
        "relative_imports",
        "postponed_annotations",
        "format",
        "import_patterns",
        "default_class_annotation",
    )

    def __init__(self, config: GeneratorConfig):
        self.substitutions: Dict[ObjectType, Dict[str, str]] = defaultdict(dict)
        for sub in config.substitutions.substitution:
            self.substitutions[sub.type][sub.search] = sub.replace

        self.import_patterns: Dict[str, Dict[str, Set[str]]] = defaultdict(
            lambda: defaultdict(set)
        )
        self.extensions: Dict[ExtensionType, List[GeneratorExtension]] = defaultdict(
            list
        )
        for ext in config.extensions.extension:
            self.extensions[ext.type].append(ext)

            is_annotation = ext.type is ExtensionType.DECORATOR
            patterns = self.import_patterns[ext.module_path][ext.func_name]

            if is_annotation:
                patterns.add(f"@{ext.func_name}")
            else:
                patterns.update(
                    [
                        f"({ext.func_name}",
                        f" {ext.func_name})",
                    ]
                )

        self.class_case: Callable = config.conventions.class_name.case
        self.field_case: Callable = config.conventions.field_name.case
        self.constant_case: Callable = config.conventions.constant_name.case
        self.package_case: Callable = config.conventions.package_name.case
        self.module_case: Callable = config.conventions.module_name.case
        self.class_safe_prefix: str = config.conventions.class_name.safe_prefix
        self.field_safe_prefix: str = config.conventions.field_name.safe_prefix
        self.constant_safe_prefix: str = config.conventions.constant_name.safe_prefix
        self.package_safe_prefix: str = config.conventions.package_name.safe_prefix
        self.module_safe_prefix: str = config.conventions.module_name.safe_prefix
        self.docstring_style: DocstringStyle = config.output.docstring_style
        self.max_line_length: int = config.output.max_line_length
        self.union_type: bool = config.output.union_type
        self.subscriptable_types: bool = config.output.subscriptable_types
        self.relative_imports: bool = config.output.relative_imports
        self.postponed_annotations: bool = config.output.postponed_annotations
        self.format = config.output.format

        # Build things
        for module, imports in self.build_import_patterns().items():
            for imp, patterns in imports.items():
                self.import_patterns[module][imp].update(patterns)

        self.default_class_annotation = self.build_class_annotation(self.format)

    def register(self, env: Environment):
        env.globals.update(
            {
                "docstring_name": self.docstring_style.name.lower(),
            }
        )
        env.filters.update(
            {
                "field_name": self.field_name,
                "field_type": self.field_type,
                "field_default": self.field_default_value,
                "field_metadata": self.field_metadata,
                "field_definition": self.field_definition,
                "class_name": self.class_name,
                "class_bases": self.class_bases,
                "class_annotations": self.class_annotations,
                "class_params": self.class_params,
                "format_string": self.format_string,
                "format_docstring": self.format_docstring,
                "constant_name": self.constant_name,
                "constant_value": self.constant_value,
                "default_imports": self.default_imports,
                "format_metadata": self.format_metadata,
                "type_name": self.type_name,
                "text_wrap": self.text_wrap,
                "clean_docstring": self.clean_docstring,
                "import_module": self.import_module,
                "import_class": self.import_class,
            }
        )

    @classmethod
    def build_class_annotation(cls, fmt: OutputFormat) -> str:
        args = []
        if not fmt.repr:
            args.append("repr=False")
        if not fmt.eq:
            args.append("eq=False")
        if fmt.order:
            args.append("order=True")
        if fmt.unsafe_hash:
            args.append("unsafe_hash=True")
        if fmt.frozen:
            args.append("frozen=True")
        if fmt.slots:
            args.append("slots=True")
        if fmt.kw_only:
            args.append("kw_only=True")

        return f"@dataclass({', '.join(args)})" if args else "@dataclass"

    def class_params(self, obj: Class):
        is_enum = obj.is_enumeration
        for attr in obj.attrs:
            name = attr.name
            docstring = self.clean_docstring(attr.help)
            if is_enum:
                yield self.constant_name(name, obj.name), docstring
            else:
                yield self.field_name(name, obj.name), docstring

    def class_name(self, name: str) -> str:
        """Convert the given string to a class name according to the selected
        conventions or use an existing alias."""
        name = self.apply_substitutions(name, ObjectType.CLASS)
        name = self.safe_name(name, self.class_safe_prefix, self.class_case)
        return self.apply_substitutions(name, ObjectType.CLASS)

    def class_bases(self, obj: Class, class_name: str) -> List[str]:
        """Return a list of base class names."""
        bases = []
        for obj_ext in obj.extensions:
            bases.append(self.type_name(obj_ext.type))

        derived = len(obj.extensions) > 0
        for ext in self.extensions[ExtensionType.CLASS]:
            is_valid = not derived or ext.apply_if_derived
            if is_valid and ext.pattern.match(class_name):
                if ext.prepend:
                    bases.insert(0, ext.func_name)
                else:
                    bases.append(ext.func_name)

        return collections.unique_sequence(bases)

    def class_annotations(self, obj: Class, class_name: str) -> List[str]:
        """Return a list of decorator names."""
        annotations = [self.default_class_annotation]

        derived = len(obj.extensions) > 0
        for ext in self.extensions[ExtensionType.DECORATOR]:
            is_valid = not derived or ext.apply_if_derived
            if is_valid and ext.pattern.match(class_name):
                if ext.prepend:
                    annotations.insert(0, f"@{ext.func_name}")
                else:
                    annotations.append(f"@{ext.func_name}")

        return collections.unique_sequence(annotations)

    def apply_substitutions(self, name: str, obj_type: ObjectType) -> str:
        for search, replace in self.substitutions[obj_type].items():
            name = re.sub(rf"{search}", rf"{replace}", name)

        return name

    def field_definition(
        self,
        attr: Attr,
        ns_map: Dict,
        parent_namespace: Optional[str],
        parents: List[str],
    ) -> str:
        """Return the field definition with any extra metadata."""
        default_value = self.field_default_value(attr, ns_map)
        metadata = self.field_metadata(attr, parent_namespace, parents)

        kwargs: Dict[str, Any] = {}
        if attr.fixed or attr.is_prohibited:
            kwargs["init"] = False

        if default_value is not False and not attr.is_prohibited:
            key = self.FACTORY_KEY if attr.is_factory else self.DEFAULT_KEY
            kwargs[key] = default_value

        if metadata:
            kwargs["metadata"] = metadata

        return f"field({self.format_arguments(kwargs, 4)})"

    def field_name(self, name: str, class_name: str) -> str:
        """
        Convert the given name to a field name according to the selected
        conventions or use an existing alias.

        Provide the class name as context for the naming schemes.
        """
        prefix = self.field_safe_prefix
        name = self.apply_substitutions(name, ObjectType.FIELD)
        name = self.safe_name(name, prefix, self.field_case, class_name=class_name)
        return self.apply_substitutions(name, ObjectType.FIELD)

    def constant_name(self, name: str, class_name: str) -> str:
        """
        Convert the given name to a constant name according to the selected
        conventions or use an existing alias.

        Provide the class name as context for the naming schemes.
        """
        prefix = self.field_safe_prefix
        name = self.apply_substitutions(name, ObjectType.FIELD)
        name = self.safe_name(name, prefix, self.constant_case, class_name=class_name)
        return self.apply_substitutions(name, ObjectType.FIELD)

    def module_name(self, name: str) -> str:
        """Convert the given string to a module name according to the selected
        conventions or use an existing alias."""
        prefix = self.module_safe_prefix
        name = self.apply_substitutions(name, ObjectType.MODULE)
        name = self.safe_name(namespaces.clean_uri(name), prefix, self.module_case)
        return self.apply_substitutions(name, ObjectType.MODULE)

    def package_name(self, name: str) -> str:
        """Convert the given string to a package name according to the selected
        conventions or use an existing alias."""

        name = self.apply_substitutions(name, ObjectType.PACKAGE)

        if not name:
            return name

        def process_sub_package(pck: str) -> str:
            pck = self.safe_name(pck, self.package_safe_prefix, self.package_case)
            return self.apply_substitutions(pck, ObjectType.PACKAGE)

        parts = map(process_sub_package, name.split("."))
        name = ".".join(parts)

        return self.apply_substitutions(name, ObjectType.PACKAGE)

    def type_name(self, attr_type: AttrType) -> str:
        """Return native python type name or apply class name conventions."""
        datatype = attr_type.datatype
        if datatype:
            return datatype.type.__name__

        return self.class_name(attr_type.alias or attr_type.name)

    def safe_name(
        self, name: str, prefix: str, name_case: Callable, **kwargs: Any
    ) -> str:
        """Sanitize names for safe generation."""
        if not name:
            return self.safe_name(prefix, prefix, name_case, **kwargs)

        if re.match(r"^-\d*\.?\d+$", name):
            return self.safe_name(f"{prefix}_minus_{name}", prefix, name_case, **kwargs)

        slug = text.alnum(name)
        if not slug or not slug[0].isalpha():
            return self.safe_name(f"{prefix}_{name}", prefix, name_case, **kwargs)

        result = name_case(name, **kwargs)
        if text.is_reserved(result):
            return self.safe_name(f"{name}_{prefix}", prefix, name_case, **kwargs)

        return result

    def import_module(self, module: str, from_module: str) -> str:
        """Convert import module to relative path if config is enabled."""
        if self.relative_imports:
            mp = module.split(".")
            fp = from_module.split(".")
            index = 0

            # Find common parts index
            while len(mp) > index and len(fp) > index and mp[index] == fp[index]:
                index += 1

            if index > 0:
                # Replace common parts with dots
                return f"{'.' * max(1, len(fp) - index)}{'.'.join(mp[index:])}"

        return module

    def import_class(self, name: str, alias: Optional[str]) -> str:
        """Convert import class name with alias support."""
        if alias:
            return f"{self.class_name(name)} as {self.class_name(alias)}"

        return self.class_name(name)

    def field_metadata(
        self, attr: Attr, parent_namespace: Optional[str], parents: List[str]
    ) -> Dict:
        """Return a metadata dictionary for the given attribute."""

        if attr.is_prohibited:
            return {"type": XmlType.IGNORE}

        name = namespace = None

        if not attr.is_nameless and attr.local_name != self.field_name(
            attr.name, parents[-1]
        ):
            name = attr.local_name

        if parent_namespace != attr.namespace or attr.is_attribute:
            namespace = attr.namespace

        restrictions = attr.restrictions.asdict(attr.native_types)

        metadata = {
            "name": name,
            "type": attr.xml_type,
            "namespace": namespace,
            "mixed": attr.mixed,
            "choices": self.field_choices(attr, parent_namespace, parents),
            **restrictions,
        }

        if self.docstring_style == DocstringStyle.ACCESSIBLE and attr.help:
            metadata["doc"] = self.clean_docstring(attr.help, False)

        return self.filter_metadata(metadata)

    def field_choices(
        self, attr: Attr, parent_namespace: Optional[str], parents: List[str]
    ) -> Optional[Tuple]:
        """
        Return a list of metadata dictionaries for the choices of the given
        attribute.

        Return None if attribute has no choices.
        """

        if not attr.choices:
            return None

        result = []
        for choice in attr.choices:
            types = choice.native_types
            restrictions = choice.restrictions.asdict(types)
            namespace = (
                choice.namespace if parent_namespace != choice.namespace else None
            )

            metadata = {
                "name": choice.name,
                "wildcard": choice.is_wildcard,
                "type": self.choice_type(choice, parents),
                "namespace": namespace,
            }

            if choice.is_nameless:
                del metadata["name"]

            default_key = self.FACTORY_KEY if choice.is_factory else self.DEFAULT_KEY
            metadata[default_key] = self.field_default_value(choice)
            metadata.update(restrictions)

            if self.docstring_style == DocstringStyle.ACCESSIBLE and choice.help:
                metadata["doc"] = self.clean_docstring(choice.help, False)

            result.append(self.filter_metadata(metadata))

        return tuple(result)

    @classmethod
    def filter_metadata(cls, data: Dict) -> Dict:
        return {
            key: value
            for key, value in data.items()
            if value is not None and value is not False
        }

    def format_arguments(self, data: Dict, indent: int = 0) -> str:
        """Return a pretty keyword arguments representation."""
        ind = " " * indent
        fmt = "    {}{}={}"
        lines = [
            fmt.format(ind, key, self.format_metadata(value, indent + 4, key))
            for key, value in data.items()
        ]

        return "\n{}\n{}".format(",\n".join(lines), ind) if lines else ""

    def format_metadata(self, data: Any, indent: int = 0, key: str = "") -> str:
        """Prettify field metadata for code generation."""
        if isinstance(data, dict):
            return self.format_dict(data, indent)

        if collections.is_array(data):
            return self.format_iterable(data, indent)

        if isinstance(data, str):
            return self.format_string(data, indent, key, 4)

        return literal_value(data)

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
        wrap = "(\n{}\n{})" if isinstance(data, tuple) else "[\n{}\n{}]"
        return wrap.format("\n".join(lines), ind)

    def format_string(self, data: str, indent: int, key: str = "", pad: int = 0) -> str:
        """
        Return a pretty string representation of a string.

        If the total length of the input string plus indent plus the key
        length and the additional pad is more than the max line length,
        wrap the text into multiple lines, avoiding breaking long words
        """
        if data.startswith("Type[") and data.endswith("]"):
            return data if data[5] == '"' else data[5:-1]

        if data.startswith("Literal[") and data.endswith("]"):
            return data[8:-1]

        if key in (self.FACTORY_KEY, self.DEFAULT_KEY):
            return data

        if key == "pattern":
            # escape double quotes because double quotes surround the regex string
            # in the rendered output
            value = re.sub(self.UNESCAPED_DBL_QUOTE_REGEX, r'\1\\"', data)
            return f'r"{value}"'

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
            f'{" " * next_indent}"{line}"'
            for line in textwrap.wrap(
                value,
                width=self.max_line_length - next_indent - 2,  # plus quotes
                drop_whitespace=False,
                replace_whitespace=False,
                break_long_words=True,
            )
        )
        return f"(\n{value}\n{' ' * indent})"

    def text_wrap(
        self, string: str, offset: int = 0, subsequent_indent: str = "    "
    ) -> str:
        """Wrap text in respect to the max line length and the given offset."""
        return "\n".join(
            textwrap.wrap(
                string,
                width=self.max_line_length - offset,
                drop_whitespace=True,
                replace_whitespace=True,
                break_long_words=False,
                subsequent_indent=subsequent_indent,
            )
        )

    @classmethod
    def clean_docstring(cls, string: Optional[str], escape: bool = True) -> str:
        """
        Prepare string for docstring generation.

        - Strip whitespace from each line
        - Replace triple double quotes with single quotes
        - Escape backslashes

        :param string: input value
        :param escape: skip backslashes escape, if string is going to
            pass through formatting.
        """
        if not string:
            return ""

        def _clean(txt: str) -> str:
            if escape:
                txt = txt.replace("\\", "\\\\")

            return txt.replace('"""', "'''").strip()

        return "\n".join(_clean(line) for line in string.splitlines() if line.strip())

    def format_docstring(self, doc_string: str, level: int) -> str:
        """Format doc strings."""
        sep_pos = doc_string.rfind('"""')
        if sep_pos == -1:
            return ""

        content = doc_string[:sep_pos]
        params = doc_string[sep_pos + 3 :].strip()

        if content.strip() == '"""' and not params:
            return ""

        content += ' """' if content.endswith('"') else '"""'

        max_length = self.max_line_length - level * 4
        configurator = configuration.Configurater(
            [
                "--wrap-summaries",
                str(max_length - 3),
                "--wrap-descriptions",
                str(max_length - 7),
                "--make-summary-multi-line",
            ]
        )
        configurator.do_parse_arguments()
        formatter = format.Formatter(
            configurator.args,
            sys.stderr,
            sys.stdin,
            sys.stdout,
        )
        content = formatter._do_format_code(content)

        if params:
            # Remove trailing triple quotes
            content = content[:-3].strip()
            new_lines = "\n" if content.endswith('"""') else "\n\n"
            content += f'{new_lines}{params}\n"""'

        return content

    def field_default_value(self, attr: Attr, ns_map: Optional[Dict] = None) -> Any:
        """Generate the field default value/factory for the given attribute."""
        if attr.is_list or (attr.is_tokens and not attr.default):
            return "tuple" if self.format.frozen else "list"
        if attr.is_dict:
            return "dict"
        if attr.default is None:
            return False if self.format.kw_only and not attr.is_optional else None
        if not isinstance(attr.default, str):
            return literal_value(attr.default)
        if attr.default.startswith("@enum@"):
            return self.field_default_enum(attr)

        types = converter.sort_types(attr.native_types)

        if attr.is_tokens:
            return self.field_default_tokens(attr, types, ns_map)

        return literal_value(
            converter.deserialize(
                attr.default, types, ns_map=ns_map, format=attr.restrictions.format
            )
        )

    def field_default_enum(self, attr: Attr) -> str:
        assert attr.default is not None

        qname, reference = attr.default[6:].split("::", 1)
        qname = next(x.alias or qname for x in attr.types if x.qname == qname)
        name = namespaces.local_name(qname)
        class_name = self.class_name(name)

        if attr.is_tokens:
            members = [
                f"Literal[{class_name}.{self.constant_name(member, name)}]"
                for member in reference.split("@")
            ]
            return f"lambda: {self.format_metadata(members, indent=8)}"

        return f"{class_name}.{self.constant_name(reference, name)}"

    def field_default_tokens(
        self, attr: Attr, types: List[Type], ns_map: Optional[Dict]
    ) -> str:
        assert isinstance(attr.default, str)

        fmt = attr.restrictions.format
        factory = tuple if self.format.frozen else list
        tokens = factory(
            converter.deserialize(val, types, ns_map=ns_map, format=fmt)
            for val in attr.default.split()
        )

        if attr.is_enumeration:
            return self.format_metadata(tuple(tokens), indent=8)

        return f"lambda: {self.format_metadata(tokens, indent=8)}"

    def field_type(self, attr: Attr, parents: List[str]) -> str:
        """Generate type hints for the given attribute."""

        if attr.is_prohibited:
            return "Any"

        type_names = collections.unique_sequence(
            self.field_type_name(x, parents) for x in attr.types
        )

        if self.union_type:
            result = " | ".join(type_names)
        else:
            result = ", ".join(type_names)
            if len(type_names) > 1:
                result = f"Union[{result}]"

        iterable = "Tuple[{}, ...]" if self.format.frozen else "List[{}]"
        if self.subscriptable_types:
            iterable = iterable.lower()

        if attr.is_tokens:
            result = iterable.format(result)

        if attr.is_list:
            return iterable.format(result)

        if attr.is_tokens:
            return result

        if attr.is_dict:
            return "dict[str, str]" if self.subscriptable_types else "Dict[str, str]"

        if attr.is_nillable or (
            attr.default is None and (attr.is_optional or not self.format.kw_only)
        ):
            return f"None | {result}" if self.union_type else f"Optional[{result}]"

        return result

    def choice_type(self, choice: Attr, parents: List[str]) -> str:
        """
        Generate type hints for the given choice.

        Choices support a subset of features from normal attributes.
        First of all we don't have a proper type hint but a type
        metadata key. That's why we always need to wrap as Type[xxx].
        The second big difference is that our choice belongs to a
        compound field that might be a list, that's why list restriction
        is also ignored.
        """
        type_names = collections.unique_sequence(
            self.field_type_name(x, parents) for x in choice.types
        )

        if self.union_type:
            result = " | ".join(type_names)
        else:
            result = ", ".join(type_names)
            if len(type_names) > 1:
                result = f"Union[{result}]"

        if choice.is_tokens:
            iterable = "Tuple[{}, ...]" if self.format.frozen else "List[{}]"
            if self.subscriptable_types:
                iterable = iterable.lower()

            result = iterable.format(result)

        if self.subscriptable_types:
            return f"type[{result}]"

        return f"Type[{result}]"

    def field_type_name(self, attr_type: AttrType, parents: List[str]) -> str:
        name = self.type_name(attr_type)

        if attr_type.forward and attr_type.circular:
            outer_str = ".".join(map(self.class_name, parents))
            name = f'"{outer_str}"'
        elif attr_type.forward:
            outer_str = ".".join(map(self.class_name, parents))
            name = f'"{outer_str}.{name}"'
        elif attr_type.circular:
            name = f'"{name}"'

        if self.postponed_annotations:
            name = name.strip('"')

        return name

    def constant_value(self, attr: Attr) -> str:
        """Return the attr default value or type as constant value."""
        attr_type = attr.types[0]
        if attr_type.native:
            return f'"{attr.default}"'

        if attr_type.alias:
            return self.class_name(attr_type.alias)

        return self.type_name(attr_type)

    def default_imports(self, output: str) -> str:
        """Generate the default imports for the given package output."""
        result = []

        if self.postponed_annotations:
            result.append("from __future__ import annotations")

        for library, types in self.import_patterns.items():
            names = [
                name
                for name, searches in types.items()
                if any(search in output for search in searches)
            ]

            if len(names) == 1 and names[0] == "__module__":
                result.append(f"import {library}")
            elif names:
                result.append(f"from {library} import {', '.join(names)}")

        return "\n".join(sorted(result))

    @classmethod
    def build_import_patterns(cls) -> Dict[str, Dict]:
        type_patterns = cls.build_type_patterns
        return {
            "dataclasses": {"dataclass": ["@dataclass"], "field": [" = field("]},
            "decimal": {"Decimal": type_patterns("Decimal")},
            "enum": {"Enum": ["(Enum)"]},
            "typing": {
                "Dict": [": Dict"],
                "List": [": List["],
                "Optional": ["Optional["],
                "Tuple": ["Tuple["],
                "Type": ["Type["],
                "Union": ["Union["],
                "Any": type_patterns("Any"),
            },
            "xml.etree.ElementTree": {"QName": type_patterns("QName")},
            "xsdata.models.datatype": {
                "XmlDate": type_patterns("XmlDate"),
                "XmlDateTime": type_patterns("XmlDateTime"),
                "XmlDuration": type_patterns("XmlDuration"),
                "XmlPeriod": type_patterns("XmlPeriod"),
                "XmlTime": type_patterns("XmlTime"),
            },
        }

    @classmethod
    def build_type_patterns(cls, x: str) -> Tuple:
        return (
            f": {x} =",
            f"[{x}]",
            f"[{x},",
            f" {x},",
            f" {x}]",
            f" {x}(",
            f" | {x}",
            f"{x} |",
        )
