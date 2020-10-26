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
    "      -",
]

custom_classes = {
    "Decimal": "decimal.Decimal",
    "QName": "xml.etree.ElementTree",
}


for tp, data_types in group_by(list(DataType), key=lambda x: x.local_name).items():
    output.append(f"    * - :class:`{custom_classes.get(tp, tp)}`")

    count = 0
    for dt in data_types:
        output.append(f"      - {dt.code}")
        count += 1
        if count == 5:
            output.append("    * -")
            count = 0

    output.extend(["      -" for _ in range(5 - count)])

output.append("    * - :class:`enum.Enum`")
output.append("      - enumeration")
output.append("      -")
output.append("      -")
output.append("      -")
output.append("      -")
output.append("")

docs_root.joinpath("data_types_table.rst").write_text(
    "\n".join(output), encoding="utf-8"
)
