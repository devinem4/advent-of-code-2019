import pytest

from monitoring_station.monitoring_station import SpaceMap


def run_test_case(map, best_loc_x, best_loc_y, asteroid_ct):
    with open(f"tests/monitoring_station_maps/{ map }") as f:
        m = SpaceMap(f.read())
    x, y = m.station.x, m.station.y
    assert best_loc_x == x
    assert best_loc_y == y
    assert asteroid_ct == m.count_visible_asteroids(x, y)


class TestFuelCounterUpper:
    def test_calc_fuel_req(self):
        run_test_case("tc1", 3, 4, 8)
        run_test_case("tc2", 5, 8, 33)
        run_test_case("tc3", 1, 2, 35)
        run_test_case("tc4", 6, 3, 41)
        run_test_case("tc5", 11, 13, 210)
