from unittest import TestCase

import pytest
from click.testing import CliRunner

from xsdata import cli


@pytest.mark.skip("Integration test")
class IntegrationTests(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        super(IntegrationTests, self).setUp()

    def test_travelport_air_kernel(self):
        self.runner.invoke(
            cli,
            [
                "generate",
                "./xsd/travelport/air_v48_0/AirReqRsp.xsd",
                "--target",
                "./target",
            ],
            catch_exceptions=False
        )
        import tests.target.air_v48_0.air_req_rsp

    def test_amadeus_fare_master_pricer(self):
        self.runner.invoke(
            cli,
            [
                "generate",
                "./xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd",
                "--target",
                "./target",
            ],
            catch_exceptions=False
        )
        import tests.target.fare_master_pricer_travel_board_search_15_3_1_a
