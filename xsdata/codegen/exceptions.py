from typing import IO, Any, Optional

from click import ClickException, echo


class CodegenWarning(Warning):
    """Recovered errors during code generation recovered errors."""


class CodegenError(ClickException):
    """Unexpected state during code generation related errors."""

    def __init__(self, message: str, **kwargs: Any):
        """Click exception constructor with metadata."""
        super().__init__(message)
        self.meta = kwargs

    def show(self, file: Optional[IO[Any]] = None) -> None:
        """Echo codegen error message and details."""
        echo("=========")
        super().show(file)
        for key, value in self.meta.items():
            echo(f"{key}: {value}")
