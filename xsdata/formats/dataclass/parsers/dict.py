import warnings
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Type, Union

from xsdata.exceptions import ConverterWarning, ParserError
from xsdata.formats.bindings import T
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta, XmlVar
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.formats.dataclass.typing import get_args, get_origin
from xsdata.utils import collections
from xsdata.utils.constants import EMPTY_MAP


@dataclass
class DictDecoder:
    """Bind a dictionary or a list of dictionaries to data models.

    Args:
        config: Parser configuration
        context: The models context instance
    """

    config: ParserConfig = field(default_factory=ParserConfig)
    context: XmlContext = field(default_factory=XmlContext)

    def decode(self, data: Union[List, Dict], clazz: Optional[Type[T]] = None) -> T:
        """Parse the input stream into the target class type.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            data: A dictionary or list of dictionaries
            clazz: The target class type to decode the input data

        Returns:
            An instance of the specified class representing the decoded content.
        """
        tp = self.verify_type(clazz, data)

        with warnings.catch_warnings():
            if self.config.fail_on_converter_warnings:
                warnings.filterwarnings("error", category=ConverterWarning)

            try:
                if not isinstance(data, list):
                    return self.bind_dataclass(data, tp)

                return [self.bind_dataclass(obj, tp) for obj in data]  # type: ignore
            except ConverterWarning as e:
                raise ParserError(e)

    def verify_type(self, clazz: Optional[Type[T]], data: Union[Dict, List]) -> Type[T]:
        """Verify the given data matches the given clazz.

        If no clazz is provided, the binding context will try
        to locate it from imported dataclasses.

        Args:
            clazz: The target class type to parse  object
            data: The loaded dictionary or list of dictionaries

        Returns:
            The clazz type to bind the loaded data.
        """
        if clazz is None:
            return self.detect_type(data)

        try:
            origin = get_origin(clazz)
            list_type = False
            if origin is list:
                list_type = True
                args = get_args(clazz)

                if len(args) != 1 or not self.context.class_type.is_model(args[0]):
                    raise TypeError()

                clazz = args[0]
            elif origin is not None:
                raise TypeError()
        except TypeError:
            raise ParserError(f"Invalid clazz argument: {clazz}")

        if list_type != isinstance(data, list):
            if list_type:
                raise ParserError("Document is object, expected array")
            raise ParserError("Document is array, expected object")

        return clazz  # type: ignore

    def detect_type(self, data: Union[Dict, List]) -> Type[T]:
        """Locate the target clazz type from the data keys.

        Args:
            data: The loaded dictionary or list of dictionaries

        Returns:
            The clazz type to bind the loaded data.
        """
        if not data:
            raise ParserError("Document is empty, can not detect type")

        keys = data[0].keys() if isinstance(data, list) else data.keys()
        clazz: Optional[Type[T]] = self.context.find_type_by_fields(set(keys))

        if clazz:
            return clazz

        raise ParserError(f"Unable to locate model with properties({list(keys)})")

    def bind_dataclass(self, data: Dict, clazz: Type[T]) -> T:
        """Create a new instance of the given class type with the given data.

        Args:
            data: The loaded data
            clazz: The target class type to bind the input data

        Returns:
            An instance of the class type representing the parsed content.
        """
        if set(data.keys()) == self.context.class_type.derived_keys:
            return self.bind_derived_dataclass(data, clazz)

        meta = self.context.build(clazz)
        xml_vars = meta.get_all_vars()

        params = {}
        for key, value in data.items():
            is_array = collections.is_array(value)
            var = self.find_var(xml_vars, key, is_array)

            if var is None and self.config.fail_on_unknown_properties:
                raise ParserError(f"Unknown property {clazz.__qualname__}.{key}")

            if var and var.init:
                params[var.name] = self.bind_value(meta, var, value)

        try:
            return self.config.class_factory(clazz, params)
        except TypeError as e:
            raise ParserError(e)

    def bind_derived_dataclass(self, data: Dict, clazz: Type[T]) -> Any:
        """Bind the input data to the given class type.

        Examples:
            >>> {
                "qname": "foo",
                "type": "my:type",
                "value": {"prop": "value"}
            }

        Args:
            data: The derived element dictionary
            clazz: The target class type to bind the input data

        Returns:
            An instance of the class type representing the parsed content.
        """
        qname = data["qname"]
        xsi_type = data["type"]
        params = data["value"]

        generic = self.context.class_type.derived_element

        if clazz is generic:
            real_clazz: Optional[Type[T]] = None
            if xsi_type:
                real_clazz = self.context.find_type(xsi_type)

            if real_clazz is None:
                raise ParserError(
                    f"Unable to locate derived model "
                    f"with properties({list(params.keys())})"
                )

            value = self.bind_dataclass(params, real_clazz)
        else:
            value = self.bind_dataclass(params, clazz)

        return generic(qname=qname, type=xsi_type, value=value)

    def bind_best_dataclass(self, data: Dict, classes: Iterable[Type[T]]) -> T:
        """Bind the input data to all the given classes and return best match.

        Args:
            data: The derived element dictionary
            classes: The target class types to try

        Returns:
            An instance of one of the class types representing the parsed content.
        """
        obj = None
        keys = set(data.keys())
        max_score = -1.0
        for clazz in classes:
            if not self.context.class_type.is_model(clazz):
                continue

            if self.context.local_names_match(keys, clazz):
                candidate = self.bind_optional_dataclass(data, clazz)
                score = self.context.class_type.score_object(candidate)
                if score > max_score:
                    max_score = score
                    obj = candidate

        if obj:
            return obj

        raise ParserError(
            f"Failed to bind object with properties({list(data.keys())}) "
            f"to any of the {[cls.__qualname__ for cls in classes]}"
        )

    def bind_optional_dataclass(self, data: Dict, clazz: Type[T]) -> Optional[T]:
        """Bind the input data to the given class type.

        This is a strict process, if there is any warning the process
        returns None. This method is used to test if te data fit into
        the class type.

        Args:
            data: The derived element dictionary
            clazz: The target class type to bind the input data

        Returns:
            An instance of the class type representing the parsed content
            or None if there is any warning or error.
        """
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("error", category=ConverterWarning)
                return self.bind_dataclass(data, clazz)
        except Exception:
            return None

    def bind_value(
        self,
        meta: XmlMeta,
        var: XmlVar,
        value: Any,
        recursive: bool = False,
    ) -> Any:
        """Main entry point for binding values.

        Args:
            meta: The parent xml meta instance
            var: The xml var descriptor for the field
            value: The data value
            recursive: Whether this is a recursive call

        Returns:
            The parsed object
        """
        # xs:anyAttributes get it out of the way, it's the mapping exception!
        if var.is_attributes:
            return dict(value)

        # Repeating element, recursively bind the values
        if not recursive and var.list_element and isinstance(value, list):
            assert var.factory is not None
            return var.factory(
                self.bind_value(meta, var, val, recursive=True) for val in value
            )

        # If not dict this is a text or tokens value.
        if not isinstance(value, dict):
            return self.bind_text(meta, var, value)

        keys = value.keys()
        if keys == self.context.class_type.any_keys:
            # Bind data to AnyElement dataclass
            return self.bind_dataclass(value, self.context.class_type.any_element)

        if keys == self.context.class_type.derived_keys:
            # Bind data to AnyElement dataclass
            return self.bind_derived_value(meta, var, value)

        # Bind data to a user defined dataclass
        return self.bind_complex_type(meta, var, value)

    def bind_text(self, meta: XmlMeta, var: XmlVar, value: Any) -> Any:
        """Bind text/tokens value entrypoint.

        Args:
            meta: The parent xml meta instance
            var: The xml var descriptor for the field
            value: The data value

        Returns:
            The parsed tokens or text value.
        """
        if var.is_elements:
            # Compound field we need to match the value to one of the choice elements
            check_subclass = self.context.class_type.is_model(value)
            choice = var.find_value_choice(value, check_subclass)
            if choice:
                return self.bind_text(meta, choice, value)

            if value is None:
                return value

            raise ParserError(
                f"Failed to bind '{value}' "
                f"to {meta.clazz.__qualname__}.{var.name} field"
            )

        if var.any_type or var.is_wildcard:
            # field can support any object return the value as it is
            return value

        value = converter.serialize(value)

        # Convert value according to the field types
        return ParserUtils.parse_value(
            value=value,
            types=var.types,
            default=var.default,
            ns_map=EMPTY_MAP,
            tokens_factory=var.tokens_factory,
            format=var.format,
        )

    def bind_complex_type(self, meta: XmlMeta, var: XmlVar, data: Dict) -> Any:
        """Bind complex values entrypoint.

        Args:
            meta: The parent xml meta instance
            var: The xml var descriptor for the field
            data: The complex data value

        Returns:
            The parsed dataclass instance.
        """
        if var.is_clazz_union:
            # Union of dataclasses
            return self.bind_best_dataclass(data, var.types)
        if var.elements:
            # Compound field with multiple choices
            return self.bind_best_dataclass(data, var.element_types)
        if var.any_type or var.is_wildcard:
            # xs:anyType element, check all meta classes
            return self.bind_best_dataclass(data, meta.element_types)

        assert var.clazz is not None

        subclasses = set(self.context.get_subclasses(var.clazz))
        if subclasses:
            # field annotation is an abstract/base type
            subclasses.add(var.clazz)
            return self.bind_best_dataclass(data, subclasses)

        return self.bind_dataclass(data, var.clazz)

    def bind_derived_value(self, meta: XmlMeta, var: XmlVar, data: Dict) -> Any:
        """Bind derived data entrypoint.

        The data is representation of a derived element, e.g. {
            "qname": "foo",
            "type": "my:type"
            "value": Any
        }

        The data value can be a primitive value or a complex value.

        Args:
            meta: The parent xml meta instance
            var: The xml var descriptor for the field
            data: The derived element data

        Returns:
            The parsed object.
        """
        qname = data["qname"]
        xsi_type = data["type"]
        params = data["value"]

        if var.elements:
            choice = var.find_choice(qname)
            if choice is None:
                raise ParserError(
                    f"Unable to locate compound element"
                    f" {meta.clazz.__qualname__}.{var.name}[{qname}]"
                )
            return self.bind_derived_value(meta, choice, data)

        if not isinstance(params, dict):
            # Is this scenario still possible???
            value = self.bind_text(meta, var, params)
        elif xsi_type:
            clazz: Optional[Type] = self.context.find_type(xsi_type)

            if clazz is None:
                raise ParserError(f"Unable to locate xsi:type `{xsi_type}`")

            value = self.bind_dataclass(params, clazz)
        elif var.clazz:
            value = self.bind_complex_type(meta, var, params)
        else:
            value = self.bind_best_dataclass(params, meta.element_types)

        generic = self.context.class_type.derived_element
        return generic(qname=qname, value=value, type=xsi_type)

    @classmethod
    def find_var(
        cls,
        xml_vars: List[XmlVar],
        local_name: str,
        is_list: bool = False,
    ) -> Optional[XmlVar]:
        """Match the name to a xml variable.

        Args:
            xml_vars: A list of xml vars
            local_name: A key from the loaded data
            is_list: Whether the data value is an array

        Returns:
            One of the xml vars, if all search attributes match, None otherwise.
        """
        for var in xml_vars:
            if var.local_name == local_name:
                var_is_list = var.list_element or var.tokens
                if is_list == var_is_list or var.clazz is None:
                    return var

        return None
