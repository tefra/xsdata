.. list-table::
    :widths: auto
    :header-rows: 1
    :align: left

    * - Python
      - XML Type
      -
      -
      -
      -
    * - :class:`bool`
      - boolean
      -
      -
      -
      -
    * - :class:`bytes`
      - base64Binary
      - hexBinary
      -
      -
      -
    * - :class:`~decimal.Decimal`
      - decimal
      -
      -
      -
      -
    * - :class:`float`
      - double
      - float
      -
      -
      -
    * - :class:`int`
      - byte
      - int
      - integer
      - long
      - negativeInteger
    * -
      - nonNegativeInteger
      - nonPositiveInteger
      - positiveInteger
      - short
      - unsignedByte
    * -
      - unsignedInt
      - unsignedLong
      - unsignedShort
      -
      -
    * - :class:`object`
      - anySimpleType
      - anyType
      -
      -
      -
    * - :class:`~xml.etree.ElementTree.QName`
      - NOTATION
      - QName
      -
      -
      -
    * - :class:`str`
      - anyAtomicType
      - anyURI
      - base
      - derivationControl
      - ENTITIES
    * -
      - ENTITY
      - error
      - ID
      - IDREF
      - IDREFS
    * -
      - lang
      - language
      - Name
      - NCName
      - NMTOKEN
    * -
      - NMTOKENS
      - normalizedString
      - simpleDerivationSet
      - string
      - token
    * - :class:`~xsdata.models.datatype.XmlDate`
      - date
      -
      -
      -
      -
    * - :class:`~xsdata.models.datatype.XmlDateTime`
      - dateTime
      - dateTimeStamp
      -
      -
      -
    * - :class:`~xsdata.models.datatype.XmlDuration`
      - dayTimeDuration
      - yearMonthDuration
      - duration
      -
      -
    * - :class:`~xsdata.models.datatype.XmlPeriod`
      - gDay
      - gMonth
      - gMonthDay
      - gYear
      - gYearMonth
    * - :class:`~xsdata.models.datatype.XmlTime`
      - time
      -
      -
      -
      -
    * - :class:`enum.Enum`
      - enumeration
      -
      -
      -
      -
