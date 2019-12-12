from math import atan2


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


class SpaceMap:
    def __init__(self, map_str):
        self.map_str = map_str
        self.convert_map()
        self.make_asteroid_list()
        self.find_best_location()
        self.laser_angle = 0

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


if __name__ == "__main__":
    with open("inputs/day10") as f:
        m = SpaceMap(f.read())

    x, y = m.station.x, m.station.y
    print(f"best loc = { x }, { y }, { len(m.angle_dict.keys()) } asteroids")
