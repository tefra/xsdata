from tests.fixtures.compound.models import Alpha
from tests.fixtures.compound.models import Bravo
from tests.fixtures.compound.models import Root


obj = Root(
    alpha_or_bravo_or_charlie=[
        Alpha(

        ),
        Alpha(

        ),
        Bravo(

        ),
        Bravo(

        ),
        Alpha(

        ),
        Bravo(

        ),
        Alpha(

        ),
        [
            'a',
            'b',
            'c',
        ],
        Bravo(

        ),
        [
            'd',
            'e',
            'f',
        ],
    ]
)
