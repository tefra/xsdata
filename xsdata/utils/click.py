import enum
import logging
from dataclasses import fields
from dataclasses import is_dataclass
from typing import Any
from typing import Callable
from typing import Dict
from typing import get_type_hints
from typing import Iterator
from typing import List
from typing import Type
from typing import TypeVar
from typing import Union

import click
from click import Command

from xsdata.codegen.writer import CodeWriter
from xsdata.utils import text

F = TypeVar("F", bound=Callable[..., Any])
FC = TypeVar("FC", Callable[..., Any], Command)


def model_options(obj: Any) -> Callable[[FC], FC]:
    def decorator(f: F) -> F:
        for option in reversed(list(build_options(obj, ""))):
            option(f)
        return f

    return decorator


def build_options(obj: Any, parent: str) -> Iterator[Callable[[FC], FC]]:
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

            yield click.option(
                *names,
                help=doc_hint,
                is_flag=is_flag,
                type=opt_type,
                default=None,
            )


def get_doc_hints(obj: Any) -> Dict[str, str]:
    result = {}
    for line in obj.__doc__.split(":param "):
        if line[0].isalpha():
            param, hint = line.split(":", 1)
            result[param] = " ".join(hint.split())

    return result


class EnumChoice(click.Choice):
    def __init__(self, enumeration: Type[enum.Enum]):
        self.enumeration = enumeration
        super().__init__([e.value for e in enumeration])

    def convert(self, value: Any, *args: Any) -> enum.Enum:
        return self.enumeration(value)


class LogFormatter(logging.Formatter):
    colors: Dict[str, Any] = {
        "error": {"fg": "red"},
        "exception": {"fg": "red"},
        "critical": {"fg": "red"},
        "debug": {"fg": "blue"},
        "warning": {"fg": "yellow"},
    }

    def format(self, record: logging.LogRecord) -> str:
        if not record.exc_info:
            level = record.levelname.lower()
            msg = record.getMessage()
            if level in self.colors:
                prefix = click.style(f"{level}", **self.colors[level])
                msg = f"{prefix}: {msg}"
            return msg

        return super().format(record)  # pragma: no cover


class LogHandler(logging.Handler):
    def __init__(self, level: Union[int, str] = logging.NOTSET):
        super().__init__(level)
        self.warnings: List[str] = []

    def emit(self, record: logging.LogRecord):
        try:
            msg = self.format(record)
            if record.levelno > logging.INFO:
                self.warnings.append(msg)
            else:
                click.echo(msg, err=True)
        except Exception:  # pragma: no cover
            self.handleError(record)

    def emit_warnings(self):
        num = len(self.warnings)
        if num:
            click.echo(click.style(f"Warnings: {num}", bold=True))
            for msg in self.warnings:
                click.echo(msg, err=True)

            self.warnings.clear()
