--8<-- "./README.md:3"

!!! Hint "Why naive?"

    The W3C XML Schema is too complicated but with good reason. It needs to support any
    api design. On the other hand when you consume xml you don't necessarily care about
    any of that. This is where xsData comes in, to simplify things by making a lot of
    assumptions like the following one that started everything:


        All xs:schema elements are classes everything else is either noise or class properties
