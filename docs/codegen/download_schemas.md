# Download Schemas

Generating from remote resources is not a great idea, the cli includes a command to
download schemas and wsdl locally. The command will download any included schemas
recursively.

```console exec="1" source="console"
$ xsdata download --help
```

**Example**

```console
❯ xsdata download https://www.w3.org/Math/XMLSchema/mathml3/mathml3.xsd -o ~/schemas
========= xsdata v24.6.1 / Python 3.11.8 / Platform linux =========

Setting base path to https:/www.w3.org/Math/XMLSchema/mathml3
Fetching https://www.w3.org/Math/XMLSchema/mathml3/mathml3.xsd
Fetching https://www.w3.org/Math/XMLSchema/mathml3/mathml3-content.xsd
Fetching https://www.w3.org/Math/XMLSchema/mathml3/mathml3-strict-content.xsd
Writing /home/chris/schemas/mathml3-strict-content.xsd
Writing /home/chris/schemas/mathml3-content.xsd
Fetching https://www.w3.org/Math/XMLSchema/mathml3/mathml3-presentation.xsd
Writing /home/chris/schemas/mathml3-presentation.xsd
Fetching https://www.w3.org/Math/XMLSchema/mathml3/mathml3-common.xsd
Writing /home/chris/schemas/mathml3-common.xsd
Writing /home/chris/schemas/mathml3.xsd
```
