import warnings
from contextlib import contextmanager
from typing import Callable, Tuple, Type, Union


@contextmanager
def warning_transform(func: Callable[[str], str],
                      warning_types: Union[Type[Warning],
                                           Tuple[Type[Warning],
                                                 ...]] = Warning):
    """
    Transform messages of the warnings emitted inside the context.

    :param func: Transformation to apply to messages
    :param warning_types: Warnings to apply to
    """
    updated_warnings = list()
    with warnings.catch_warnings(record=True) as w:
        yield
        for warning in w:
            if isinstance(warning.message, warning_types):
                payload, *rest = warning.message.args
                payload = func(payload)
                warning.message.args = (payload, *rest)
            updated_warnings.append(warning)
    for warning in updated_warnings:
        warnings.warn_explicit(warning.message,
                               warning.category,
                               warning.filename,
                               warning.lineno,
                               source=warning.source)
