from collections import defaultdict
from pathlib import Path

from tests.conftest import read_root_name

here = Path(__file__).parent
tests = here.parent.parent
fixtures = here.parent.joinpath("fixtures")

test_case = """def test_{name}():
    schema = "{path}"
    package = "{package}"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
"""

integration_test_case = """def test_integration():

    schema = Path("{path}")
    package = "{package}"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "{clazz}")
    validate_bindings(schema, clazz)
"""

test_file = """import os
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import load_class
from tests.conftest import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


{output}"""

test_file_simple = """import os
from pathlib import Path

from click.testing import CliRunner

from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


{output}"""


def generate():
    schemas = defaultdict(list)
    for xsd in fixtures.glob("defxmlschema/*/*.xsd"):
        schemas[xsd.parent.name].append(xsd)

    for chapter, xsds in schemas.items():

        output = list()
        simple_output = True
        for xsd in sorted(xsds):
            path = xsd.relative_to(tests)
            package = ".".join(path.parent.parts)
            package = f"{package.replace('.xsd', '')}"
            name = xsd.stem
            if xsd.stem.startswith("example"):
                output.append(test_case.format(name=name, path=path, package=package))
            elif xsd.stem.startswith("chapter"):
                instance = xsd.with_suffix(".xml")
                if instance.exists():
                    simple_output = False
                    output.append(
                        integration_test_case.format(
                            name=name,
                            path=path,
                            package=package,
                            clazz=read_root_name(instance),
                        )
                    )

        tpl = test_file_simple if simple_output else test_file
        module = tpl.format(output="\n\n".join(output))
        file = here.joinpath(f"test_{chapter}.py")
        file.write_text(module)
        print(f"Writing: {file}")


if __name__ == "__main__":
    generate()
