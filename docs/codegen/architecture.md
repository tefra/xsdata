# Architecture

The [ResourceTransformer][xsdata.codegen.transformer.ResourceTransformer] is the
orchestrator of the code generation procedure.

```mermaid
graph LR
    A[Load Resources] --> B(Parse transfer objects)
    B --> C[Convert to classes]
    C --> D[Analyze classes]
    D--> E[Write Output]
```

## Load Resource

The code generator accepts URIs indicating either local or remote file locations.

The resource type (xsd, wsdl, dtd, xml, json) is identified based on the file extension,
if present. If the resource lacks an extension, the loader will attempt to locate
specific syntax markings associated with the resource type.

If a resource cannot be accessed, a warning is issued, and the program continues its
normal flow. In the case of circular imports, resources are loaded only once.

## Parse transfer objects

A resource-specific parser is utilized to bind document information to transfer objects.
Additionally, the parsers are responsible for assigning common values required for later
analysis, such as locations, a namespace prefix-URI map, and common namespaces like xsi
and xlink.

- XSD: [SchemaParser][xsdata.codegen.parsers.SchemaParser]
- DTD: [DtdParser][xsdata.codegen.parsers.DtdParser]
- WSDL: [DefinitionsParser][xsdata.codegen.parsers.DefinitionsParser]
- XML: [TreeParser][xsdata.formats.dataclass.parsers.TreeParser]
- JSON: [json.loads][]

## Convert to classes

A resource-specific parser is utilized to convert the transfer objects to codegen
classes. These mappers encapsulate the pertinent logic detailing how the resource types
should be interpreted.

- XSD: [SchemaMapper][xsdata.codegen.mappers.SchemaMapper]
- DTD: [DtdMapper][xsdata.codegen.mappers.DtdMapper]
- WSDL: [DefinitionsMapper][xsdata.codegen.mappers.DefinitionsMapper]
- XML: [ElementMapper][xsdata.codegen.mappers.ElementMapper]
- JSON: [DictMapper][xsdata.codegen.mappers.DictMapper]

## Analyze classes

```mermaid
graph LR
    A[Validate classes] --> B(Process classes)
    B --> C[Validate class references]
```

### Validate Classes

- Remove types with unknown references

```xml
<xs:element name="root" ref="xs:missingOrUnknown"/>
```

- Remove duplicate types: Keep the last definition

```xml
<xs:element name="root" ref="RootType"/>
<xs:element name="root" ref="RootType"/>
```

- Remove duplicate overridden types:

```xml
<xs:override schemaLocation="over005a.xsd">
    <xs:attribute name="code" type="xs:date"/>
</xs:override>
```

- Merge redefined types:

```xml
<xs:redefine schemaLocation="schZ006.xsd">
    <xs:group name="GCustomDimProps">
        <xs:sequence>
            <xs:element name="DisplayInfo"	type="xs:unsignedInt"/>
        </xs:sequence>
    </xs:group>
</xs:redefine>
```

API: [xsdata.codegen.validator.ClassValidator][]

### Analyze Classes

The classes are wrapped in a [ClassContainer][xsdata.codegen.container.ClassContainer]
instance. It includes some easy finder methods and orchestrates flattening/filtering
processes.

The process is divided into multiple steps and handlers per step. All classes have to
pass through each step before next one starts. The order of the steps is very important!

### Step: Ungroup

- [FlattenAttributeGroups][xsdata.codegen.handlers.FlattenAttributeGroups]

### Step: Flatten

- [CalculateAttributePaths][xsdata.codegen.handlers.CalculateAttributePaths]
- [FlattenClassExtensions][xsdata.codegen.handlers.FlattenClassExtensions]
- [SanitizeEnumerationClass][xsdata.codegen.handlers.SanitizeEnumerationClass]
- [UpdateAttributesEffectiveChoice][xsdata.codegen.handlers.UpdateAttributesEffectiveChoice]
- [UnnestInnerClasses][xsdata.codegen.handlers.UnnestInnerClasses]
- [AddAttributeSubstitutions][xsdata.codegen.handlers.AddAttributeSubstitutions]
- [ProcessAttributeTypes][xsdata.codegen.handlers.ProcessAttributeTypes]
- [MergeAttributes][xsdata.codegen.handlers.MergeAttributes]
- [ProcessMixedContentClass][xsdata.codegen.handlers.ProcessMixedContentClass]

### Step: Filer

- [FilterClasses][xsdata.codegen.handlers.FilterClasses]

### Step: Sanitize

- [ResetAttributeSequences][xsdata.codegen.handlers.ResetAttributeSequences]
- [RenameDuplicateAttributes][xsdata.codegen.handlers.RenameDuplicateAttributes]
- [SanitizeAttributesDefaultValue][xsdata.codegen.handlers.SanitizeAttributesDefaultValue]

### Step: Resolve

- [ValidateAttributesOverrides][xsdata.codegen.handlers.ValidateAttributesOverrides]

### Step: Vacuum

- [VacuumInnerClasses][xsdata.codegen.handlers.VacuumInnerClasses]

### Step: Finalize

- [DetectCircularReferences][xsdata.codegen.handlers.DetectCircularReferences]
- [CreateCompoundFields][xsdata.codegen.handlers.CreateCompoundFields]
- [CreateWrapperFields][xsdata.codegen.handlers.CreateWrapperFields]
- [DisambiguateChoices][xsdata.codegen.handlers.DisambiguateChoices]
- [ResetAttributeSequenceNumbers][xsdata.codegen.handlers.ResetAttributeSequenceNumbers]

### Step: Designate

- [RenameDuplicateClasses][xsdata.codegen.handlers.RenameDuplicateClasses]
- [ValidateReferences][xsdata.codegen.handlers.ValidateReferences]
- [DesignateClassPackages][xsdata.codegen.handlers.DesignateClassPackages]
