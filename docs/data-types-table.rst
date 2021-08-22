.. list-table::
    :widths: auto
    :header-rows: 1
    :align: left

    * - Python
      - XML Type
      -
      -
      -
    * - :class:`bool`
      - boolean
      -
      -
      -
    * - :class:`bytes`
      - hexBinary
      - base64Binary
      -
      -
    * - :class:`~decimal.Decimal`
      - decimal
      -
      -
      -
    * - :class:`float`
      - float
      - double
      -
      -
    * - :class:`int`
      - integer
      - nonPositiveInteger
      - negativeInteger
      - long
    * -
      - int
      - short
      - byte
      - nonNegativeInteger
    * -
      - unsignedLong
      - unsignedInt
      - unsignedShort
      - unsignedByte
    * -
      - positiveInteger
      -
      -
      -
    * - :class:`object`
      - anyType
      - anySimpleType
      -
      -
    * - :class:`~xml.etree.ElementTree.QName`
      - QName
      - NOTATION
      -
      -
    * - :class:`str`
      - string
      - anyURI
      - normalizedString
      - token
    * -
      - language
      - NMTOKEN
      - NMTOKENS
      - Name
    * -
      - NCName
      - ID
      - IDREF
      - IDREFS
    * -
      - ENTITIES
      - ENTITY
      - anyAtomicType
      - error
    * - :class:`~xsdata.models.datatype.XmlDate`
      - date
      -
      -
      -
    * - :class:`~xsdata.models.datatype.XmlDateTime`
      - dateTime
      - dateTimeStamp
      -
      -
    * - :class:`~xsdata.models.datatype.XmlDuration`
      - duration
      - dayTimeDuration
      - yearMonthDuration
      -
    * - :class:`~xsdata.models.datatype.XmlPeriod`
      - gYearMonth
      - gYear
      - gMonthDay
      - gMonth
    * -
      - gDay
      -
      -
      -
    * - :class:`~xsdata.models.datatype.XmlTime`
      - time
      -
      -
      -
    * - :class:`enum.Enum`
      - enumeration
      -
      -
      -
