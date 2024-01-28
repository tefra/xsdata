from pathlib import Path

import mkdocs_gen_files

src = Path(__file__).parent.parent.parent / "xsdata"
nav = mkdocs_gen_files.Nav()


for path in sorted(src.rglob("*.py")):
    module_path = path.relative_to(src).with_suffix("")

    parts = tuple(module_path.parts)

    if parts[-1] in ("__init__", "__main__"):
        continue

    doc_path = path.relative_to(src).with_suffix(".md")
    full_doc_path = Path("api", doc_path)

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)
        print("::: xsdata." + identifier, file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path)


with mkdocs_gen_files.open("api/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
