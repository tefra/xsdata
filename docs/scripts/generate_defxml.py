from collections import defaultdict
from pathlib import Path
from typing import Dict

docs_root = Path(__file__).parent.parent
docs_root.joinpath("defxmlschema").mkdir(parents=True, exist_ok=True)
fixtures = docs_root.joinpath("../tests/fixtures")

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

bind_tpl = """

**Schema**

.. literalinclude:: /{input}
   :language: xml
   :lines: 2-

**Models**

.. literalinclude:: /{output}
   :language: python

**XML Document**

.. literalinclude:: /{instance}
   :language: xml
   :lines: 2-

**xsData XML Document**

.. literalinclude:: /{xsdata_instance}
   :language: xml
   :lines: 2-

**xsData JSON**

.. literalinclude:: /{xsdata_json}
   :language: json"""

chapter_tpl = """{title}

{output}

.. admonition:: Samples Source
    :class: hint

    `Definitive XML Schema <http://www.datypic.com/books/defxmlschema/>`_
    by Priscilla Walmsley (c) 2012 Prentice Hall PTR
"""


def generate():
    schemas = list(fixtures.glob("defxmlschema/chapter*.xsd"))
    if len(schemas) == 0:
        raise Exception(fixtures.as_uri())

    for xsd in schemas:

        if len(xsd.stem) != 9:
            continue

        buffer = []
        section_titles.clear()

        if not xsd.with_suffix(".py").exists():
            continue

        input = xsd.relative_to(docs_root)
        output = input.with_suffix(".py")

        if xsd.with_suffix(".xml").exists():
            buffer.append(
                bind_tpl.format(
                    input=input,
                    output=output,
                    instance=input.with_suffix(".xml"),
                    xsdata_instance=input.with_suffix(".xsdata.xml"),
                    xsdata_json=input.with_suffix(".json"),
                )
            )

        chapter = xsd.stem
        number = chapter.replace("chapter", "#")
        title = "{number} - {topic}".format(number=number, topic=subtitles[chapter])
        title = "{line}\n{title}\n{line}".format(line="*" * len(title), title=title)

        file = docs_root.joinpath(f"defxmlschema/{chapter}.rst")
        file.write_text(
            chapter_tpl.format(title=title, output="\n\n".join(buffer)),
            encoding="utf-8",
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
        parts = title.split()
        for i in range(len(parts)):
            if parts[i][0].isdigit():
                parts[i] += f".{section_titles[title]}"
        title = " ".join(parts)

    return title


generate()
