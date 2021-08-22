import shlex
import subprocess
from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import TYPE_CHECKING

from docutils import nodes
from docutils.nodes import Element
from docutils.nodes import Node
from docutils.parsers.rst import directives  # type: ignore
from sphinx.directives.code import container_wrapper
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util import parselinenos
from sphinx.util.docutils import SphinxDirective
from sphinx.util.typing import OptionSpec

if TYPE_CHECKING:
    from sphinx.application import Sphinx

logger = logging.getLogger(__name__)


class CLI(SphinxDirective):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec: OptionSpec = {
        "force": directives.flag,
        "language": directives.unchanged_required,
        "lines": directives.unchanged_required,
        "caption": directives.unchanged,
        "class": directives.class_option,
        "name": directives.unchanged,
    }

    def run(self) -> List[Node]:
        document = self.state.document

        try:
            location = self.state_machine.get_source_and_line(self.lineno)
            output = self.execute()
            output = self.lines_filter(f"{self.arguments[0]}\n{output}", location)

            literal: Element = nodes.literal_block(output, output)
            literal["force"] = "force" in self.options

            self.set_source_info(literal)
            self.add_name(literal)

            literal["language"] = self.options.get("language", "text")
            literal["classes"] += self.options.get("class", [])

            caption = self.options.get("caption")
            if caption:
                literal = container_wrapper(self, literal, caption)

            return [literal]
        except Exception as exc:
            return [document.reporter.warning(exc, line=self.lineno)]

    def execute(self) -> str:
        args = shlex.split(self.arguments[0])
        out, err = subprocess.Popen(
            args,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        ).communicate()
        return out.decode()

    def lines_filter(self, text: str, location: Tuple[str, int] = None) -> str:
        linespec = self.options.get("lines")
        if linespec:
            lines = text.splitlines(True)
            linelist = parselinenos(linespec, len(lines))
            if any(i >= len(lines) for i in linelist):
                logger.warning(
                    __("line number spec is out of range(1-%d): %r")
                    % (len(lines), linespec),
                    location=location,
                )

            text = "".join(lines[n] for n in linelist if n < len(lines))

        return text


def setup(app: "Sphinx") -> Dict[str, Any]:
    directives.register_directive("cli", CLI)

    return {
        "version": "builtin",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
