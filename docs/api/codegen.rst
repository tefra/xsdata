================
Generator Config
================

The configuration offers more advance options to further tail the output to your needs,
like naming conventions and substitutions.

.. warning::

    Since v21.12 the aliases were replaced by the substitutions config which is a more
    flexible search and replace process with support for regular expressions.

    During initialization aliases will be migrated to substitutions and the config
    will be automatically updated, but you should also verify you still get the desired
    output.


.. cli:: xsdata init-config --print
    :language: xml
    :lines: 3-

.. currentmodule:: xsdata.models.config

.. autosummary::
    :toctree: reference
    :template: dataclass.rst
    :nosignatures:

    GeneratorConfig
    GeneratorOutput

    OutputFormat
    GeneratorConventions
    GeneratorSubstitutions
    GeneratorExtensions
    StructureStyle
    DocstringStyle
    ClassFilterStrategy
    CompoundFields
    ObjectType
    ExtensionType
    GeneratorSubstitution
    GeneratorExtension
    NameConvention
    NameCase
