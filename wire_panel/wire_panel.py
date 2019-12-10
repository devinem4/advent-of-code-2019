class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({ self.x }, { self.y })"

    def __repr__(self):
        return str(self)

    @staticmethod
    def min_manhattan_dist(points):
        mh_dist = 999999999  # max int?
        for p in points:
            mh_dist = min(mh_dist, abs(p.x) + abs(p.y))

        return mh_dist


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"L: { self.p1 } -> { self.p2 }"

    def __repr__(self):
        return str(self)

    @staticmethod
    def intersection(line1, line2):
        # assumes vertical and horizontal lines only
        # returns a point that is the intersection of the two lines

        # when line1 horizontal (line 2 must be vertical for a intersection)
        if (
            (min(line1.p1.x, line1.p2.x) < line2.p1.x)
            and (max(line1.p1.x, line1.p2.x) > line2.p1.x)
            and (min(line2.p1.y, line2.p2.y) < line1.p1.y)
            and (max(line2.p1.y, line2.p2.y) > line1.p1.y)
        ):
            return Point(line2.p1.x, line1.p1.y)

        # when line1 vertical (line 2 must be horizontal for a intersection)
        if (
            (min(line1.p1.y, line1.p2.y) < line2.p1.y)
            and (max(line1.p1.y, line1.p2.y) > line2.p1.y)
            and (min(line2.p1.x, line2.p2.x) < line1.p1.x)
            and (max(line2.p1.x, line2.p2.x) > line1.p1.x)
        ):
            return Point(line1.p1.x, line2.p1.y)

        return None

    def point_on_line(self, point):
        # return number of steps from line.p1 to point if true, else none

        # horizontal line
        if (
            min(self.p1.x, self.p2.x) < point.x < max(self.p1.x, self.p2.x)
            and point.y == self.p1.y
        ):
            return abs(point.x - self.p1.x)
        # vertical self
        if (
            min(self.p1.y, self.p2.y) < point.y < max(self.p1.y, self.p2.y)
            and point.x == self.p1.x
        ):
            return abs(point.y - self.p1.y)


class Wire:
    def __init__(self, wire: str):
        self.wire_str = wire
        self.lines = self.get_lines()

    def __str__(self):
        return self.wire_str

    def __repr__(self):
        return str(self)

    def get_lines(self):
        p1 = Point(0, 0)  # start at the origin
        lines = []
        for path in self.wire_str.split(","):
            direction = path[0]
            magnitude = int(path[1:])
            if direction == "U":
                p2 = Point(p1.x, p1.y + magnitude)
            elif direction == "D":
                p2 = Point(p1.x, p1.y - magnitude)
            elif direction == "R":
                p2 = Point(p1.x + magnitude, p1.y)
            elif direction == "L":
                p2 = Point(p1.x - magnitude, p1.y)
            lines.append(Line(p1, p2))
            p1 = p2
        return lines

    def steps_to_point(self, point):
        # roll through each line on this wire until we reach the point
        # keep a running sum of the steps until we get there
        steps = 0
        for line in self.lines:
            pol = line.point_on_line(point)
            if pol:
                return steps + pol
            steps += abs(line.p1.x - line.p2.x) + abs(line.p1.y - line.p2.y)

        # never found the point on the line
        return None


class Panel:
    def __init__(self, wires):
        # assuming two strings of wires are coming in
        self.wire_1 = Wire(wires.split("\n")[0])
        self.wire_2 = Wire(wires.split("\n")[1])
        self.intersections = self.find_intersections()
        self.mh_dist = Point.min_manhattan_dist(self.intersections)
        self.min_steps = self.calc_min_steps()

    def find_intersections(self):
        intersections = []
        for line1 in self.wire_1.lines:
            for line2 in self.wire_2.lines:
                p = Line.intersection(line1, line2)
                if p:
                    intersections.append(p)
        return intersections

    def calc_min_steps(self):
        min_steps = 99999999999
        for intersect in self.intersections:
            new_steps = self.wire_1.steps_to_point(
                intersect
            ) + self.wire_2.steps_to_point(intersect)
            min_steps = min(min_steps, new_steps)

        return min_steps


if __name__ == "__main__":
    with open("inputs/day03") as f:
        wires = f.read()

    p = Panel(wires)
    print(f"manhattan distance = { p.mh_dist }")
    print(f"min steps = { p.min_steps }")
