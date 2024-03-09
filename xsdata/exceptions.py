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


class ClientValueError(ValueError):
    """Client related errors."""
