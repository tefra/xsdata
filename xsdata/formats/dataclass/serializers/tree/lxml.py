from dataclasses import dataclass

from lxml.etree import Element, TreeBuilder

from xsdata.formats.dataclass.serializers.tree.mixins import TreeSerializer
from xsdata.formats.types import T


@dataclass
class LxmlTreeSerializer(TreeSerializer):
    def render(self, obj: T) -> Element:
        """Serialize the input model instance to element tree.

        Args:
            obj: The input model instance to serialize

        Returns:
            The generated element tree instance.
        """
        builder = TreeBuilder()
        self.build(obj, builder)
        return builder.close()
