from tests.fixtures.wrapper.models import Charlie
from tests.fixtures.wrapper.models import Wrapper


obj = Wrapper(
    alpha='ααα',
    bravo=[
        1,
        2,
    ],
    charlie=[
        Charlie(
            value='δδδ',
            lang='en'
        ),
        Charlie(
            value='eee',
            lang='en'
        ),
    ]
)
