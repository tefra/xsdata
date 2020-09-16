from lxml import etree


def pretty_xml(xml: str) -> str:
    tree = etree.XML(xml.encode(), etree.XMLParser(remove_blank_text=True))
    return etree.tostring(
        tree, pretty_print=True, xml_declaration=True, encoding="UTF-8"
    ).decode()
