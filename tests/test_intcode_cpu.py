import pytest

from intcode_cpu.intcode_cpu import IntcodeCpu


def run_test_case(initial_state, exp):
    icpu = IntcodeCpu(initial_state)
    assert exp == icpu.process()


class TestFuelCounterUpper:
    def test_calc_fuel_req(self):
        run_test_case("1,0,0,0,99", "2,0,0,0,99")
        run_test_case("2,3,0,3,99", "2,3,0,6,99")
        run_test_case("2,4,4,5,99,0", "2,4,4,5,99,9801")
        run_test_case("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")
