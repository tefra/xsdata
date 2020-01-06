# ./x.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2020-01-06 11:11:22.290106 by PyXB version 1.2.7-DEV using Python 3.7.4.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals

import io

import pyxb
import pyxb.binding

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import pyxb.binding.saxer
import pyxb.utils.domutils
import pyxb.utils.six as _six
import pyxb.utils.utility

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    "urn:uuid:81e881e8-3064-11ea-9f1c-000c293dfa64"
)

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.7-DEV"
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()


# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(["typeBinding", "elementBinding"])


def CreateFromDocument(
    xml_text,
    fallback_namespace=None,
    location_base=None,
    default_namespace=None,
):
    """
    Parse the given XML and use the document element to create a Python
    instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=fallback_namespace, location_base=location_base
    )
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, fallback_namespace=None, default_namespace=None):
    """
    Create a Python instance from the given DOM node. The node tag must
    correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}.
    """
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(
        node, fallback_namespace
    )


# Atomic simple type: [anonymous]
class STD_ANON(pyxb.binding.datatypes.positiveInteger):
    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 44, 14
    )
    _Documentation = None


STD_ANON._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(
    value_datatype=pyxb.binding.datatypes.positiveInteger,
    value=pyxb.binding.datatypes.nonNegativeInteger(100),
)
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxExclusive)
_module_typeBindings.STD_ANON = STD_ANON


# Atomic simple type: SKU
class SKU(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "SKU")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 61, 2
    )
    _Documentation = None


SKU._CF_pattern = pyxb.binding.facets.CF_pattern()
SKU._CF_pattern.addPattern(pattern="\\d{3}-[A-Z]{2}")
SKU._InitializeFacetMap(SKU._CF_pattern)
Namespace.addCategoryObject("typeBinding", "SKU", SKU)
_module_typeBindings.SKU = SKU


# Complex type PurchaseOrderType with content type ELEMENT_ONLY
class PurchaseOrderType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type PurchaseOrderType with content type ELEMENT_ONLY."""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "PurchaseOrderType")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 15, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "comment"),
        "comment",
        "__AbsentNamespace0_PurchaseOrderType_comment",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 13, 2
        ),
    )

    comment = property(__comment.value, __comment.set, None, None)

    # Element shipTo uses Python identifier shipTo
    __shipTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "shipTo"),
        "shipTo",
        "__AbsentNamespace0_PurchaseOrderType_shipTo",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 17, 6
        ),
    )

    shipTo = property(__shipTo.value, __shipTo.set, None, None)

    # Element billTo uses Python identifier billTo
    __billTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "billTo"),
        "billTo",
        "__AbsentNamespace0_PurchaseOrderType_billTo",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 18, 6
        ),
    )

    billTo = property(__billTo.value, __billTo.set, None, None)

    # Element items uses Python identifier items
    __items = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "items"),
        "items",
        "__AbsentNamespace0_PurchaseOrderType_items",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 20, 6
        ),
    )

    items = property(__items.value, __items.set, None, None)

    # Attribute orderDate uses Python identifier orderDate
    __orderDate = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "orderDate"),
        "orderDate",
        "__AbsentNamespace0_PurchaseOrderType_orderDate",
        pyxb.binding.datatypes.date,
    )
    __orderDate._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 22, 4
    )
    __orderDate._UseLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 22, 4
    )

    orderDate = property(__orderDate.value, __orderDate.set, None, None)

    _ElementMap.update(
        {
            __comment.name(): __comment,
            __shipTo.name(): __shipTo,
            __billTo.name(): __billTo,
            __items.name(): __items,
        }
    )
    _AttributeMap.update({__orderDate.name(): __orderDate})


_module_typeBindings.PurchaseOrderType = PurchaseOrderType
Namespace.addCategoryObject(
    "typeBinding", "PurchaseOrderType", PurchaseOrderType
)


# Complex type USAddress with content type ELEMENT_ONLY
class USAddress(pyxb.binding.basis.complexTypeDefinition):
    """Complex type USAddress with content type ELEMENT_ONLY."""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "USAddress")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 25, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "name"),
        "name",
        "__AbsentNamespace0_USAddress_name",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 27, 6
        ),
    )

    name = property(__name.value, __name.set, None, None)

    # Element street uses Python identifier street
    __street = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "street"),
        "street",
        "__AbsentNamespace0_USAddress_street",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 28, 6
        ),
    )

    street = property(__street.value, __street.set, None, None)

    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "city"),
        "city",
        "__AbsentNamespace0_USAddress_city",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 29, 6
        ),
    )

    city = property(__city.value, __city.set, None, None)

    # Element state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "state"),
        "state",
        "__AbsentNamespace0_USAddress_state",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 30, 6
        ),
    )

    state = property(__state.value, __state.set, None, None)

    # Element zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "zip"),
        "zip",
        "__AbsentNamespace0_USAddress_zip",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 31, 6
        ),
    )

    zip = property(__zip.value, __zip.set, None, None)

    # Attribute country uses Python identifier country
    __country = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "country"),
        "country",
        "__AbsentNamespace0_USAddress_country",
        pyxb.binding.datatypes.NMTOKEN,
        fixed=True,
        unicode_default="US",
    )
    __country._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 33, 4
    )
    __country._UseLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 33, 4
    )

    country = property(__country.value, __country.set, None, None)

    _ElementMap.update(
        {
            __name.name(): __name,
            __street.name(): __street,
            __city.name(): __city,
            __state.name(): __state,
            __zip.name(): __zip,
        }
    )
    _AttributeMap.update({__country.name(): __country})


_module_typeBindings.USAddress = USAddress
Namespace.addCategoryObject("typeBinding", "USAddress", USAddress)


# Complex type Items with content type ELEMENT_ONLY
class Items(pyxb.binding.basis.complexTypeDefinition):
    """Complex type Items with content type ELEMENT_ONLY."""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Items")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 37, 2
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element item uses Python identifier item
    __item = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "item"),
        "item",
        "__AbsentNamespace0_Items_item",
        True,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 39, 6
        ),
    )

    item = property(__item.value, __item.set, None, None)

    _ElementMap.update({__item.name(): __item})
    _AttributeMap.update({})


_module_typeBindings.Items = Items
Namespace.addCategoryObject("typeBinding", "Items", Items)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY."""

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 40, 8
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, "comment"),
        "comment",
        "__AbsentNamespace0_CTD_ANON_comment",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 13, 2
        ),
    )

    comment = property(__comment.value, __comment.set, None, None)

    # Element productName uses Python identifier productName
    __productName = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "productName"),
        "productName",
        "__AbsentNamespace0_CTD_ANON_productName",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 42, 12
        ),
    )

    productName = property(__productName.value, __productName.set, None, None)

    # Element quantity uses Python identifier quantity
    __quantity = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "quantity"),
        "quantity",
        "__AbsentNamespace0_CTD_ANON_quantity",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 43, 12
        ),
    )

    quantity = property(__quantity.value, __quantity.set, None, None)

    # Element USPrice uses Python identifier USPrice
    __USPrice = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "USPrice"),
        "USPrice",
        "__AbsentNamespace0_CTD_ANON_USPrice",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 50, 12
        ),
    )

    USPrice = property(__USPrice.value, __USPrice.set, None, None)

    # Element shipDate uses Python identifier shipDate
    __shipDate = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "shipDate"),
        "shipDate",
        "__AbsentNamespace0_CTD_ANON_shipDate",
        False,
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 52, 12
        ),
    )

    shipDate = property(__shipDate.value, __shipDate.set, None, None)

    # Attribute partNum uses Python identifier partNum
    __partNum = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "partNum"),
        "partNum",
        "__AbsentNamespace0_CTD_ANON_partNum",
        _module_typeBindings.SKU,
        required=True,
    )
    __partNum._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 54, 10
    )
    __partNum._UseLocation = pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 54, 10
    )

    partNum = property(__partNum.value, __partNum.set, None, None)

    _ElementMap.update(
        {
            __comment.name(): __comment,
            __productName.name(): __productName,
            __quantity.name(): __quantity,
            __USPrice.name(): __USPrice,
            __shipDate.name(): __shipDate,
        }
    )
    _AttributeMap.update({__partNum.name(): __partNum})


_module_typeBindings.CTD_ANON = CTD_ANON

comment = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "comment"),
    pyxb.binding.datatypes.string,
    location=pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 13, 2
    ),
)
Namespace.addCategoryObject(
    "elementBinding", comment.name().localName(), comment
)

purchaseOrder = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "purchaseOrder"),
    PurchaseOrderType,
    location=pyxb.utils.utility.Location(
        "/home/chris/projects/xsdata/docs/examples/primer.xsd", 11, 2
    ),
)
Namespace.addCategoryObject(
    "elementBinding", purchaseOrder.name().localName(), purchaseOrder
)

PurchaseOrderType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "comment"),
        pyxb.binding.datatypes.string,
        scope=PurchaseOrderType,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 13, 2
        ),
    )
)

PurchaseOrderType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "shipTo"),
        USAddress,
        scope=PurchaseOrderType,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 17, 6
        ),
    )
)

PurchaseOrderType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "billTo"),
        USAddress,
        scope=PurchaseOrderType,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 18, 6
        ),
    )
)

PurchaseOrderType._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "items"),
        Items,
        scope=PurchaseOrderType,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 20, 6
        ),
    )
)


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 19, 6
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PurchaseOrderType._UseForTag(
            pyxb.namespace.ExpandedName(None, "shipTo")
        ),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 17, 6
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PurchaseOrderType._UseForTag(
            pyxb.namespace.ExpandedName(None, "billTo")
        ),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 18, 6
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PurchaseOrderType._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, "comment")
        ),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 19, 6
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        PurchaseOrderType._UseForTag(
            pyxb.namespace.ExpandedName(None, "items")
        ),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 20, 6
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(
        fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)])
    )
    transitions.append(
        fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)])
    )
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


PurchaseOrderType._Automaton = _BuildAutomaton()

USAddress._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "name"),
        pyxb.binding.datatypes.string,
        scope=USAddress,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 27, 6
        ),
    )
)

USAddress._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "street"),
        pyxb.binding.datatypes.string,
        scope=USAddress,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 28, 6
        ),
    )
)

USAddress._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "city"),
        pyxb.binding.datatypes.string,
        scope=USAddress,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 29, 6
        ),
    )
)

USAddress._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "state"),
        pyxb.binding.datatypes.string,
        scope=USAddress,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 30, 6
        ),
    )
)

USAddress._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "zip"),
        pyxb.binding.datatypes.decimal,
        scope=USAddress,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 31, 6
        ),
    )
)


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        USAddress._UseForTag(pyxb.namespace.ExpandedName(None, "name")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 27, 6
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        USAddress._UseForTag(pyxb.namespace.ExpandedName(None, "street")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 28, 6
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        USAddress._UseForTag(pyxb.namespace.ExpandedName(None, "city")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 29, 6
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        USAddress._UseForTag(pyxb.namespace.ExpandedName(None, "state")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 30, 6
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        USAddress._UseForTag(pyxb.namespace.ExpandedName(None, "zip")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 31, 6
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


USAddress._Automaton = _BuildAutomaton_()

Items._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "item"),
        CTD_ANON,
        scope=Items,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 39, 6
        ),
    )
)


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 39, 6
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Items._UseForTag(pyxb.namespace.ExpandedName(None, "item")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 39, 6
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    transitions.append(
        fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)])
    )
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Items._Automaton = _BuildAutomaton_2()

CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(Namespace, "comment"),
        pyxb.binding.datatypes.string,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 13, 2
        ),
    )
)

CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "productName"),
        pyxb.binding.datatypes.string,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 42, 12
        ),
    )
)

CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "quantity"),
        STD_ANON,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 43, 12
        ),
    )
)

CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "USPrice"),
        pyxb.binding.datatypes.decimal,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 50, 12
        ),
    )
)

CTD_ANON._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "shipDate"),
        pyxb.binding.datatypes.date,
        scope=CTD_ANON,
        location=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 52, 12
        ),
    )
)


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 51, 12
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 52, 12
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, "productName")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 42, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, "quantity")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 43, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, "USPrice")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 50, 12
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, "comment")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 51, 12
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, "shipDate")),
        pyxb.utils.utility.Location(
            "/home/chris/projects/xsdata/docs/examples/primer.xsd", 52, 12
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(
        fac.Transition(st_3, [fac.UpdateInstruction(cc_0, True)])
    )
    transitions.append(
        fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)])
    )
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(
        fac.Transition(st_4, [fac.UpdateInstruction(cc_1, True)])
    )
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON._Automaton = _BuildAutomaton_3()
