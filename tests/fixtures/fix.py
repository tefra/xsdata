from pathlib import Path

root_start = "<xs:schema xmlns:xs=\"http://www.w3.org/2001/XMLSchema\">"
root_end = "</xs:schema>"

files = Path(__file__).parent.glob("defxmlschema/*/*.xsd")
for xsd in files:

    content = xsd.read_text()
    if ":schema" not in content:
        lines = content.split("\n")
        pos = next(idx for idx, line in enumerate(lines) if not line.strip().startswith("<!--"))
        lines.insert(pos, root_start)
        lines.append(root_end)

        xsd.write_text("\n".join(lines), encoding="utf-8")

    if "-" in xsd.name:
        name = xsd.name.replace("-", "")
        dir = xsd.parent
        new_path = dir.joinpath(name)

        xsd.rename(new_path)