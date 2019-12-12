from math import atan2, pi


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Ast({ self.x }, { self.y })"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def set_dist_from_station(self, station):
        # manhattan dist is good enough
        self.dist_from_station = abs(self.x - station.x) + abs(self.y - station.y)


class SpaceMap:
    def __init__(self, map_str):
        self.map_str = map_str
        self.convert_map()
        self.make_asteroid_list()
        self.find_best_location()

    def convert_map(self):
        """converts a map string to array of 1s (asteroids) and zeroes (empty)"""
        map_lines = self.map_str.replace(".", "0").replace("#", "1").split("\n")
        self.map = []

        for line in map_lines:
            self.map.append([int(c) for c in line])

        self.map_rows = len(self.map)
        self.map_cols = len(self.map[0])

    def make_asteroid_list(self):
        self.asteroids = []
        for y, row in enumerate(self.map):
            for x, location in enumerate(row):
                if location:
                    self.asteroids.append(Asteroid(x, y))

    def get_asteroid_angle_dict(self, pos_x, pos_y):
        """
        from position x, y -- which angles have asteroids can be seen?
        
        find all of the angles from pos_x, pos_y that hit any asteroid
        for now we don't care which one it hits
        """

        # angles from hero asteroid: [ list of asteroids at that angle ]
        angle_dict = {}

        for ast in self.asteroids:
            if ast == Asteroid(pos_x, pos_y):
                # dont check ourself
                continue

            rise = pos_y - ast.y
            run = ast.x - pos_x
            angle_to_ast = atan2(run, rise)
            if angle_to_ast < 0:
                # since we are dealing with radians, anything over 180 degrees is a negative
                # this should put the angles in clockwise order.
                angle_to_ast = 2 * 3.14159 + angle_to_ast
            asteroids_at_this_angle = angle_dict.get(angle_to_ast, [])
            asteroids_at_this_angle.append(ast)
            angle_dict[angle_to_ast] = asteroids_at_this_angle

        return angle_dict

    def find_best_location(self):
        best_asteroid = None
        most_visible = 0
        for asteroid in self.asteroids:
            angle_dict = self.get_asteroid_angle_dict(asteroid.x, asteroid.y)
            visible_ct = len(angle_dict.keys())
            # print(asteroid, visible_ct, angle_dict)
            if visible_ct > most_visible:
                best_asteroid = asteroid
                most_visible = visible_ct
                self.angle_dict = angle_dict

        self.station = best_asteroid
        for angle, asteroids in self.angle_dict.items():
            for asteroid in asteroids:
                asteroid.set_dist_from_station(best_asteroid)
            self.angle_dict[angle] = sorted(
                asteroids, key=lambda x: x.dist_from_station
            )

    def vaporize_asteroids(self, num_asteroids):
        """
        vaporize num_asteroids by firing our giant laser n times

        laser always aims up to begin, rotates to next clockwise
        asteroid after each fire.

        returns the position of the last vaporized asteroid
        """
        vaporized = 0
        while vaporized < num_asteroids:
            for angle in sorted(self.angle_dict.keys()):
                if self.angle_dict[angle]:
                    # there are un-vaporized asteroids left at this angle
                    last_vaporized = self.angle_dict[angle].pop(0)
                    vaporized += 1
                    if vaporized >= num_asteroids:
                        break
        return last_vaporized


if __name__ == "__main__":
    with open("inputs/day10") as f:
        m = SpaceMap(f.read())

    x, y = m.station.x, m.station.y
    print(f"best loc = { x }, { y }, { len(m.angle_dict.keys()) } asteroids")

    ast_200 = m.vaporize_asteroids(200)
    print(f"the 200th vaporized asteroid = { ast_200 }")
    print(f"solution = { ast_200.x * 100 + ast_200.y }")
