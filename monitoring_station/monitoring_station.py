from math import gcd


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

    def count_visible_asteroids(self, pos_x, pos_y):
        """ from position x, y -- how many asteroids can be seen? """
        # draw a line from x, y to all locations
        # find the first asteroid that intersects and add to the list

        visible_asteroids = []

        for y in range(0, self.map_rows):
            for x in range(0, self.map_cols):
                if x == pos_x and y == pos_y:
                    # looking at itself -- doesnt count
                    continue

                # print(f"checking: { x }, { y }")
                rise = pos_y - y
                run = x - pos_x
                # how many actual points on our map are on this line?
                points_on_line = gcd(rise, run)
                rise = rise / points_on_line
                run = run / points_on_line

                # print(f"    slope: { rise } / { run } -> { points_on_line }")

                for i in range(1, points_on_line + 1):
                    check_x = pos_x + run * i
                    check_y = pos_y - rise * i
                    possible_asteroid = Asteroid(check_x, check_y)

                    if possible_asteroid in self.asteroids:
                        if possible_asteroid not in visible_asteroids:
                            # new asteroid found
                            visible_asteroids.append(possible_asteroid)
                            # print(f"    added { possible_asteroid }")
                        else:
                            # old asteroid found again
                            # print(f"    already found { possible_asteroid }")
                            pass
                        break

        return len(visible_asteroids)

    def find_best_location(self):
        best_asteroid = None
        most_visible = 0
        for asteroid in self.asteroids:
            visible = self.count_visible_asteroids(asteroid.x, asteroid.y)
            print(asteroid, visible)
            if visible > most_visible:
                best_asteroid = asteroid
                most_visible = visible
        return best_asteroid.x, best_asteroid.y


if __name__ == "__main__":
    with open("inputs/day10") as f:
        m = SpaceMap(f.read())

    x, y = m.find_best_location()
    print(f"best loc = { x }, { y }, { m.count_visible_asteroids(x, y) } asteroids")
