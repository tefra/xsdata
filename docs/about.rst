About
=====

Why
---

Python soap clients are either dead or all of them follow the all-in-one pattern that hides all the complexity of the api from the end-user.

Python XML Binding libraries exist but either they never worked for the schemas I was working with or generated code that was very hard to read and understand.

xsData is inspired by the Java XML Binding JaxB and with the rise of python model classes like attrs, dataclasses or pydantic and the native python type hints, I felt it was time to create something similar for python.


Compare
-------

xsData
^^^^^^

.. code-block:: python

    @dataclass
    class PurchaseOrderType:
        """
        :ivar ship_to:
        :ivar bill_to:
        :ivar comment:
        :ivar items:
        :ivar order_date:
        """
        ship_to: Optional[Usaddress] = field(
            default=None,
            metadata=dict(
                name="shipTo",
                type="Element",
                required=True
            )
        )
        bill_to: Optional[Usaddress] = field(
            default=None,
            metadata=dict(
                name="billTo",
                type="Element",
                required=True
            )
        )
        comment: Optional[Comment] = field(
            default=None,
            metadata=dict(
                name="comment",
                type="Element"
            )
        )
        items: Optional[Items] = field(
            default=None,
            metadata=dict(
                name="items",
                type="Element",
                required=True
            )
        )
        order_date: Optional[str] = field(
            default=None,
            metadata=dict(
                name="orderDate",
                type="Attribute"
            )
        )


pyXB
^^^^

.. code-block:: python

    # Complex type PurchaseOrderType with content type ELEMENT_ONLY
    class PurchaseOrderType (pyxb.binding.basis.complexTypeDefinition):
        """Complex type PurchaseOrderType with content type ELEMENT_ONLY"""
        _TypeDefinition = None
        _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
        _Abstract = False
        _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PurchaseOrderType')
        _XSDLocation = pyxb.utils.utility.Location('/home/chris/projects/xsdata/docs/examples/primer.xsd', 15, 2)
        _ElementMap = {}
        _AttributeMap = {}
        # Base type is pyxb.binding.datatypes.anyType

        # Element comment uses Python identifier comment
        __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comment'), 'comment', '__AbsentNamespace0_PurchaseOrderType_comment', False, pyxb.utils.utility.Location('/home/chris/projects/xsdata/docs/examples/primer.xsd', 13, 2), )


        comment = property(__comment.value, __comment.set, None, None)


        # Element shipTo uses Python identifier shipTo
        __shipTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shipTo'), 'shipTo', '__AbsentNamespace0_PurchaseOrderType_shipTo', False, pyxb.utils.utility.Location('/home/chris/projects/xsdata/docs/examples/primer.xsd', 17, 6), )


        shipTo = property(__shipTo.value, __shipTo.set, None, None)


        # Element billTo uses Python identifier billTo
        __billTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'billTo'), 'billTo', '__AbsentNamespace0_PurchaseOrderType_billTo', False, pyxb.utils.utility.Location('/home/chris/projects/xsdata/docs/examples/primer.xsd', 18, 6), )


        billTo = property(__billTo.value, __billTo.set, None, None)


        # Element items uses Python identifier items
        __items = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'items'), 'items', '__AbsentNamespace0_PurchaseOrderType_items', False, pyxb.utils.utility.Location('/home/chris/projects/xsdata/docs/examples/primer.xsd', 20, 6), )


        items = property(__items.value, __items.set, None, None)


        # Attribute orderDate uses Python identifier orderDate
        __orderDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'orderDate'), 'orderDate', '__AbsentNamespace0_PurchaseOrderType_orderDate', pyxb.binding.datatypes.date)
        __orderDate._DeclarationLocation = pyxb.utils.utility.Location('/home/chris/projects/xsdata/docs/examples/primer.xsd', 22, 4)
        __orderDate._UseLocation = pyxb.utils.utility.Location('/home/chris/projects/xsdata/docs/examples/primer.xsd', 22, 4)

        orderDate = property(__orderDate.value, __orderDate.set, None, None)

        _ElementMap.update({
            __comment.name() : __comment,
            __shipTo.name() : __shipTo,
            __billTo.name() : __billTo,
            __items.name() : __items
        })
        _AttributeMap.update({
            __orderDate.name() : __orderDate
        })
    _module_typeBindings.PurchaseOrderType = PurchaseOrderType
    Namespace.addCategoryObject('typeBinding', 'PurchaseOrderType', PurchaseOrderType)


JaxB
^^^^

.. code-block:: java

    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlType(name = "PurchaseOrderType", propOrder = {
        "shipTo",
        "billTo",
        "comment",
        "items"
    })
    public class PurchaseOrderType {

        @XmlElement(required = true)
        protected USAddress shipTo;
        @XmlElement(required = true)
        protected USAddress billTo;
        protected String comment;
        @XmlElement(required = true)
        protected Items items;
        @XmlAttribute(name = "orderDate")
        @XmlSchemaType(name = "date")
        protected XMLGregorianCalendar orderDate;

        /**
         * Lots of getters/setters
         */
    }
