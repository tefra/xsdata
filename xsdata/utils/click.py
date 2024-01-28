import enum
import inspect
import logging
from dataclasses import fields, is_dataclass
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Type,
    TypeVar,
    Union,
    get_type_hints,
)

import click
from click import Command

from xsdata.codegen.writer import CodeWriter
from xsdata.utils import text

F = TypeVar("F", bound=Callable[..., Any])
FC = TypeVar("FC", Callable[..., Any], Command)


def model_options(obj: Any) -> Callable[[FC], FC]:
    """Decorate click commands to add model options."""

    def decorator(f: F) -> F:
        for option in reversed(list(build_options(obj, ""))):
            option(f)
        return f

    return decorator


def build_options(obj: Any, parent: str) -> Iterator[Callable[[FC], FC]]:
    """Build click options by a data class."""
    type_hints = get_type_hints(obj)
    doc_hints = get_doc_hints(obj)

    for field in fields(obj):
        type_hint = type_hints[field.name]
        doc_hint = doc_hints[field.name]
        name = field.metadata.get("cli", field.name)

        if not name:
            continue

        qname = f"{parent}.{field.name}".strip(".")

        if is_dataclass(type_hint):
            yield from build_options(type_hint, qname)
        else:
            is_flag = False
            opt_type = type_hint
            if name == "output":
                opt_type = click.Choice(CodeWriter.generators.keys())
                names = ["-o", "--output"]
            elif type_hint is bool:
                is_flag = True
                opt_type = None
                name = text.kebab_case(name)
                names = [f"--{name}/--no-{name}"]
            else:
                if issubclass(type_hint, enum.Enum):
                    opt_type = EnumChoice(type_hint)

                parts = text.split_words(name)
                name = "-".join(parts)
                name_short = "".join(part[0] for part in parts)
                names = [f"--{name}", f"-{name_short}"]

            names.append("__".join(qname.split(".")))

            default_value = (
                field.default.value
                if isinstance(field.default, enum.Enum)
                else field.default
            )
            doc_hint += f" [default: {default_value}]"

            yield click.option(
                *names,
                help=doc_hint,
                is_flag=is_flag,
                type=opt_type,
                default=None,
            )


def get_doc_hints(obj: Any) -> Dict[str, str]:
    """Return a param-docstring map of the class arguments."""
    docstrings = inspect.getdoc(obj)
    assert docstrings is not None

    start = docstrings.index("Args:") + 6
    params = docstrings[start:].replace("\n        ", " ")

    result = {}
    for line in params.splitlines():
        param, hint = line.split(":", 1)
        result[param.strip()] = " ".join(hint.split())

    return result


class EnumChoice(click.Choice):
    """Custom click choice widget for enumerations."""

    def __init__(self, enumeration: Type[enum.Enum]):
        self.enumeration = enumeration
        super().__init__([e.value for e in enumeration])

    def convert(self, value: Any, *args: Any) -> enum.Enum:
        """Parse the value into an enumeration member."""
        return self.enumeration(value)


class LogFormatter(logging.Formatter):
    """Custom log formatter with click colors."""

    colors: Dict[str, Any] = {
        "error": {"fg": "red"},
        "exception": {"fg": "red"},
        "critical": {"fg": "red"},
        "debug": {"fg": "blue"},
        "warning": {"fg": "yellow"},
    }

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record with click styles."""
        if not record.exc_info:
            level = record.levelname.lower()
            msg = record.getMessage()
            if level in self.colors:
                prefix = click.style(f"{level}", **self.colors[level])
                msg = f"{prefix}: {msg}"
            return msg

        return super().format(record)  # pragma: no cover


class LogHandler(logging.Handler):
    """Custom click log handler to record warnings."""

    def __init__(self, level: Union[int, str] = logging.NOTSET):
        super().__init__(level)
        self.warnings: List[str] = []

    def emit(self, record: logging.LogRecord):
        """Override emit to record warnings."""
        try:
            msg = self.format(record)
            if record.levelno > logging.INFO:
                self.warnings.append(msg)
            else:
                click.echo(msg, err=True)
        except Exception:  # pragma: no cover
            self.handleError(record)

    def emit_warnings(self):
        """Print all recorded warnings to click stdout."""
        num = len(self.warnings)
        if num:
            click.echo(click.style(f"Warnings: {num}", bold=True))
            for msg in self.warnings:
                click.echo(msg, err=True)

            self.warnings.clear()
