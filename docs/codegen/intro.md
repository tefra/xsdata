# Introduction

The code generator works with:

- XML Schemas v1.0 & v1.1
- WSDL v1.1 definitions with SOAP v1.1 bindings
- DTD external definitions
- Directly from XML and JSON Documents

The [xsdata.codegen.transformer][xsdata.codegen.transformer] will detect and switch
parsers based on the resource extension otherwise it will do some heuristic content
searches. Before you start make sure the cli requirements are installed.

```console
$ pip install xsdata[cli]
```

## Command Line Tool

```console exec="1" source="console"
$ xsdata generate --help
```

## Use a directory as source

You can instruct the cli to search all subdirectories recursively with the
`-r, --recursive` flag.

```console
$ xsdata generate project/schemas
$ xsdata generate project/schemas --recursive
```

## Use a filename or URI as source

```console
$ xsdata generate project/schemas/feed.xsd
$ xsdata generate http://www.gstatic.com/localfeed/local_feed.xsd
```
