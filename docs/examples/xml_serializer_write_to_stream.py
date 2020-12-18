import sys

from docs.examples.xml_serializer_basic import serializer, books

# write to stdout
serializer.write(sys.stdout, books, ns_map={None: "urn:books"})

# write directly to a file stream
with open("example.xml", "w") as fp:
    serializer.write(fp, books)
