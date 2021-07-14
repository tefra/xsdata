class CodeGenerationError(TypeError):
    """Unexpected state during code generation related errors."""


class CodeGenerationWarning(Warning):
    """Recovered errors during code generation recovered errors."""


class GeneratorConfigError(CodeGenerationError):
    """Unexpected state during generator config related errors."""


class ConverterError(ValueError):
    """Converting values between document/python types related errors."""


class ConverterWarning(Warning):
    """Converting values between document/python types recovered errors."""


class ParserError(ValueError):
    """Parsing related errors."""


class XmlHandlerError(ValueError):
    """Xml handler related errors."""


class XmlWriterError(ValueError):
    """Xml writer related errors."""


class SerializerError(ValueError):
    """Serializing related errors."""


class XmlContextError(ValueError):
    """Unhandled behaviour during data binding."""


class SchemaValueError(ValueError):
    """Schema definitions related errors."""


class DefinitionsValueError(ValueError):
    """Service definitions related errors."""


class AnalyzerValueError(ValueError):
    """Unhandled behaviour during class analyze process.."""


class ResolverValueError(ValueError):
    """Dependencies related errors."""


class ClientValueError(ValueError):
    """Client related errors."""
