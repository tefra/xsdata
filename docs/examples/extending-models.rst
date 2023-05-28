================
Extending Models
================



Creating subclasses from the generated models require to repeat the original `Meta`
class and it's generally discouraged. You can instead apply base classes and
decorators through the code generation configuration.


The following configuration will add a base class and a decorator to all the
generated classes.

Read :ref:`more <GeneratorExtension>`.


.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <Config xmlns="http://pypi.org/project/xsdata" version="23.6">
      <Extensions>
        <Extension type="class" class=".*" import="dataclasses_jsonschema.JsonSchemaMixin" prepend="false" applyIfDerived="false"/>
        <Extension type="decorator" class=".*" import="typed_dataclass.typed_dataclass" prepend="false" applyIfDerived="false"/>
      </Extensions>
    </Config>


.. code-block:: python

    from dataclasses import dataclass, field
    from dataclasses_jsonschema import JsonSchemaMixin
    from typed_dataclass import typed_dataclass
    from typing import Optional


    @dataclass
    @typed_dataclass
    class Cores(JsonSchemaMixin):
        class Meta:
            name = "cores"

        core: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
