class CodeGenerationError(TypeError):
    """Unexpected state during code generation related errors."""


class ConverterError(ValueError):
    """Converting values between document/python types related errors."""


class ParserError(ValueError):
    """Parsing related errors."""


class SerializerError(ValueError):
    """Serializing related errors."""


class XmlContextError(ValueError):
    """Unhandled behaviour during data binding."""


class SchemaValueError(ValueError):
    """Schema definitions related errors."""


class AnalyzerValueError(ValueError):
    """Unhandled behaviour during class analyze process.."""


class ResolverValueError(ValueError):
    """Dependencies related errors."""
