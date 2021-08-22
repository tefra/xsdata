from pathlib import Path

from xsdata.models.enums import DataType
from xsdata.utils.collections import group_by

docs_root = Path(__file__).parent.parent

output = [
    ".. list-table::",
    "    :widths: auto",
    "    :header-rows: 1",
    "    :align: left",
    "",
    "    * - Python",
    "      - XML Type",
    "      -",
    "      -",
    "      -",
]

groups = group_by(list(DataType), key=lambda x: x.type.__name__.lower())
for key in sorted(groups):
    tp = groups[key][0].type
    if tp.__module__ != "builtins":
        output.append(f"    * - :class:`~{tp.__module__}.{tp.__name__}`")
    else:
        output.append(f"    * - :class:`{tp.__name__}`")

    count = 0
    for dt in groups[key]:
        output.append(f"      - {dt.code}")
        count += 1
        if count == 4:
            output.append("    * -")
            count = 0

    if count:
        output.extend(["      -" for _ in range(4 - count)])
    else:
        output.pop()

output.append("    * - :class:`enum.Enum`")
output.append("      - enumeration")
output.append("      -")
output.append("      -")
output.append("      -")
output.append("")
result = "\n".join(output)
docs_root.joinpath("data-types-table.rst").write_text(result, encoding="utf-8")
