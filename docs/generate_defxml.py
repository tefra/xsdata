from collections import defaultdict
from pathlib import Path
from typing import Dict

here = Path(__file__).parent
root = here.parent
fixtures = here.parent.joinpath("tests/fixtures")

subtitles = {
    "chapter01": "Schemas: An introduction",
    "chapter02": "A quick tour of XML Schema",
    "chapter03": "Namespaces",
    "chapter04": "Schema composition",
    "chapter05": "Instances and schemas",
    "chapter06": "Element declarations",
    "chapter07": "Attribute declarations",
    "chapter08": "Simple types",
    "chapter09": "Regular expressions",
    "chapter10": "Union and list types",
    "chapter11": "Built-in simple types",
    "chapter12": "Complex types",
    "chapter13": "Deriving complex types",
    "chapter14": "Assertions",
    "chapter15": "Named groups",
    "chapter16": "Substitution groups",
    "chapter17": "Identity constraints",
    "chapter18": "Redefining and overriding schema components",
    "chapter19": "Topics for DTD users",
    "chapter20": "XML information modeling",
    "chapter21": "Schema design and documentation",
    "chapter22": "Extensibility and reuse",
    "chapter23": "Versioning",
}

tpl = """{title}

.. literalinclude:: /../{input}
   :language: xml
   :lines: 3-

.. literalinclude:: /../{output}
   :language: python"""

bind_tpl = """{title}

**Schema**

.. literalinclude:: /../{input}
   :language: xml
   :lines: 2-

**XML Document**

.. literalinclude:: /../{instance}
   :language: xml
   :lines: 2-

**xsData XML Document**

.. literalinclude:: /../{xsdata_instance}
   :language: xml
   :lines: 2-

**xsData JSON**

.. literalinclude:: /../{xsdata_json}
   :language: json"""

chapter_tpl = """{title}

{subtitle}

{output}

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR
"""


def generate():
    schemas = defaultdict(list)
    for xsd in fixtures.glob("defxmlschema/*/*.xsd"):
        schemas[xsd.parent.name].append(xsd)

    for chapter, xsds in schemas.items():
        buffer = list()
        section_titles.clear()

        for xsd in sorted(xsds):
            if not xsd.with_suffix(".py").exists():
                continue

            input = xsd.relative_to(root)
            output = input.with_suffix(".py")

            if xsd.stem.startswith("example"):
                title = parse_title(xsd.read_text())
                title = "{title}\n{line}".format(title=title, line="*" * len(title))
                buffer.append(tpl.format(title=title, input=input, output=output))
            elif xsd.stem.startswith("chapter"):
                if xsd.with_suffix(".xml").exists():
                    title = "Binding Test"
                    title = "{title}\n{line}".format(title=title, line="*" * len(title))
                    buffer.append(
                        bind_tpl.format(
                            title=title,
                            input=input,
                            output=output,
                            instance=input.with_suffix(".xml"),
                            xsdata_instance=input.with_suffix(".xsdata.xml"),
                            xsdata_json=input.with_suffix(".json"),
                        )
                    )

        title = chapter.replace("chapter", "Chapter ")
        title = "{line}\n{title}\n{line}".format(line="*" * len(title), title=title)
        subtitle = subtitles[chapter]
        subtitle = "{title}\n{line}".format(line="=" * len(subtitle), title=subtitle)

        file = here.joinpath(f"defxmlschema/{chapter}.rst")
        file.write_text(
            chapter_tpl.format(
                title=title, subtitle=subtitle, output="\n\n".join(buffer)
            )
        )
        print(f"Writing: {file}")


section_titles: Dict[str, int] = defaultdict(int)


def parse_title(source: str) -> str:
    pos = source.find("<!-- Example ")
    if pos == -1:
        raise Exception("title not found.")
    end = source.find("-->", pos)
    start = pos + 5
    title = source[start:end].strip()

    if title in section_titles:
        parts = title.split(" ")
        for i in range(len(parts)):
            if parts[i][0].isdigit():
                parts[i] += f".{section_titles[title]}"
        title = " ".join(parts)

    return title


if __name__ == "__main__":
    generate()
