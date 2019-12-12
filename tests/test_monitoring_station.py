import pytest

from monitoring_station.monitoring_station import SpaceMap


def run_test_case(map, best_loc_x, best_loc_y, asteroid_ct):
    with open(f"tests/monitoring_station_maps/{ map }") as f:
        m = SpaceMap(f.read())
    x, y = m.station.x, m.station.y
    assert best_loc_x == x
    assert best_loc_y == y
    assert asteroid_ct == len(m.angle_dict.keys())


def run_vaporizer_test(map, vaporize_count, exp_x, exp_y):
    with open(f"tests/monitoring_station_maps/{ map }") as f:
        m = SpaceMap(f.read())
    ast = m.vaporize_asteroids(vaporize_count)
    assert exp_x == ast.x
    assert exp_y == ast.y


class TestFindBestLocation:
    def test_find_best_location(self):
        run_test_case("tc1", 3, 4, 8)
        run_test_case("tc2", 5, 8, 33)
        run_test_case("tc3", 1, 2, 35)
        run_test_case("tc4", 6, 3, 41)
        run_test_case("tc5", 11, 13, 210)

    def test_vaporizer(self):
        run_vaporizer_test("tc5", 1, 11, 12)
        run_vaporizer_test("tc5", 2, 12, 1)
        run_vaporizer_test("tc5", 3, 12, 2)
        run_vaporizer_test("tc5", 10, 12, 8)
        run_vaporizer_test("tc5", 20, 16, 0)
        run_vaporizer_test("tc5", 50, 16, 9)
        run_vaporizer_test("tc5", 100, 10, 16)
        run_vaporizer_test("tc5", 199, 9, 6)
        run_vaporizer_test("tc5", 200, 8, 2)
        run_vaporizer_test("tc5", 201, 10, 9)
        run_vaporizer_test("tc5", 299, 11, 1)
