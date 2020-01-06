Code Generator
==============


CLI Entry Point
---------------

.. command-output:: xsdata --help

XSD Path
--------

The generator doesn't work with urls only with local files, if the given schema includes other schemas with urls the generator will fail. Every schema is evaluated once and in the order they are defined.

Circular dependencies will probably work just fine :)

Package
-------

The package option defines where the target module(s) will be created inside the current working directory.

If the main xsd has any parent include or import you should adjust the target package.

.. admonition:: Example
    :class: warning

    * Output directory ``./api/models``
    * Main xsd ``./api/air/AirReqRsp.xsd` that includes ``../common/CommonReqRsp.xsd``
    * Adjust the package from ``api.models`` to ``api.models.air`` because the generator has to also create the ``common.common_req_rsp`` module.

Renderer
--------

The renderer option changes the output format.

* ``pydata``: Python lib `dataclasses <https://docs.python.org/3/library/dataclasses.html>`_


Print
-----

The print flag bypasses the file writer and instead prints a quick preview of what the generator would create otherwise.

It's a very useful option when the class building process changes with new features.

.. admonition:: Example Output
    :class: hint

    .. code-block:: python

        samples.sabre.output.bargain_finder_max_common_types_v1_9_7.AdvResTicketingType()
            adv_res_ind: Optional[bool] = [('default', None)]
            adv_reservation: Optional["AdvResTicketingType.AdvReservation"] = [('default', None)]
            adv_ticketing: Optional["AdvResTicketingType.AdvTicketing"] = [('default', None)]
            adv_ticketing_ind: Optional[bool] = [('default', None)]

            samples.sabre.output.bargain_finder_max_common_types_v1_9_7.AdvResTicketingType.AdvReservation()
                latest_period: Optional[str] = [('default', None), ('pattern', '[0-9]{1,3}')]
                latest_time_of_day: Optional[str] = [('default', None)]
                latest_unit: Optional[StayUnitType] = [('default', None)]

            samples.sabre.output.bargain_finder_max_common_types_v1_9_7.AdvResTicketingType.AdvTicketing()
                from_depart_period: Optional[str] = [('default', None), ('pattern', '[0-9]{1,3}')]
                from_depart_time_of_day: Optional[str] = [('default', None)]
                from_depart_unit: Optional[StayUnitType] = [('default', None)]
                from_res_period: Optional[str] = [('default', None), ('pattern', '[0-9]{1,3}')]
                from_res_time_of_day: Optional[str] = [('default', None)]
                from_res_unit: Optional[StayUnitType] = [('default', None)]

        samples.sabre.output.bargain_finder_max_common_types_v1_9_7.AirTripType(str)
            CIRCLE: xs:string = [('default', '"Circle"')]
            ONE_WAY: xs:string = [('default', '"OneWay"')]
            OPEN_JAW: xs:string = [('default', '"OpenJaw"')]
            OTHER: xs:string = [('default', '"Other"')]
            RETURN_VALUE: xs:string = [('default', '"Return"')]


Verbosity
---------

The verbosity option changes what messages will be printed.

Available options: ``CRITICAL``, ``ERROR``, ``WARNING``, ``INFO`` or ``DEBUG``


Examples
--------

Check the `samples repo <https://github.com/tefra/xsdata-samples>`_ for more.


Basic
^^^^^

.. literalinclude:: examples/common.py
   :language: python
   :lines: 353-392


Enum
^^^^

.. literalinclude:: examples/common.py
   :language: python
   :lines: 1685-1702


Inner Class
^^^^^^^^^^^^

.. literalinclude:: examples/common.py
   :language: python
   :lines: 395-434
