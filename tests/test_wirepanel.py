import pytest

from wire_panel.wire_panel import Panel


def run_test_case(wires, exp, exp_steps):
    p = Panel(wires)
    assert exp == p.mh_dist
    assert exp_steps == p.min_steps


class TestFuelCounterUpper:
    def test_calc_fuel_req(self):
        run_test_case(
            "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83",
            159,
            610,
        )
        run_test_case(
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n"
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135,
            410,
        )
