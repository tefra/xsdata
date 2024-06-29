from pathlib import Path
import time
import xml.etree.ElementTree
import my_dataclass
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler


TEST_ITERATIONS = 1000
my_path = Path(__file__).parent
xml_file = my_path / "input.xml"


def main():
    with xml_file.open() as f:
        file_contents = f.read()

    start_time = time.time()
    using_in_built_element(file_contents, TEST_ITERATIONS)
    end_time = time.time()
    time_using_in_built_element = end_time - start_time
    print("Time using Python xml.etree.ElementTree.Element:", time_using_in_built_element)

    start_time = time.time()
    using_xsdata(file_contents, TEST_ITERATIONS)
    end_time = time.time()
    time_using_xsdata = end_time - start_time
    print("Time using xsdata:", time_using_xsdata)

    print ("Ratio:", time_using_xsdata / time_using_in_built_element)


def using_in_built_element(xml_string, iterations):
    for _ in range(iterations):
        xml_root = xml.etree.ElementTree.fromstring(xml_string)


def using_xsdata(xml_string, iterations):
    parser = XmlParser(handler=XmlEventHandler)
    for _ in range(iterations):
        record_as_obj = parser.from_string(xml_string, my_dataclass.LogRecord)


if __name__ == "__main__":
    main()
