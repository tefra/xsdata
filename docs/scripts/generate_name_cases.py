import re
from pathlib import Path

from xsdata.models.config import NameCase

docs_root = Path(__file__).parent.parent.resolve()
source = docs_root.parent.joinpath("tests/utils/test_text.py").read_text()


output = [
    ".. list-table::",
    "    :widths: auto",
    "    :header-rows: 1",
    "    :align: left",
    "",
    "    * - Original",
    "      - Pascal Case",
    "      - Camel Case",
    "      - Snake Case",
    "      - Mixed Case",
    "      - Mixed Snake Case",
]

result = {}
for case in NameCase:
    lookup = case.func.__name__
    result[lookup] = re.findall(
        rf"assertEqual\(\"(.*)\"\, {lookup}\(\"(.*)\"\)\)", source
    )

i = 0
while i < len(result[lookup]):
    output.append(f"    * - {result['pascal_case'][i][1]}")
    output.append(f"      - {result['pascal_case'][i][0]}")
    output.append(f"      - {result['camel_case'][i][0]}")
    output.append(f"      - {result['snake_case'][i][0]}")
    output.append(f"      - {result['mixed_case'][i][0]}")
    output.append(f"      - {result['mixed_snake_case'][i][0]}")

    i += 1

output.append("")

docs_root.joinpath("name_cases_table.rst").write_text(
    "\n".join(output), encoding="utf-8"
)
