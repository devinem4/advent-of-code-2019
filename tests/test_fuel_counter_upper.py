import pytest
from collections import namedtuple

from fuel_counter_upper.fuel_counter_upper import FuelCounterUpper


def run_test_case(mass, exp):
    fcu = FuelCounterUpper()
    assert exp == fcu.calc_fuel_req(mass)


class TestFuelCounterUpper:
    def test_calc_fuel_req(self):
        run_test_case(12, 2)
        run_test_case(14, 2)
        run_test_case(1969, 966)
        run_test_case(100756, 50346)
