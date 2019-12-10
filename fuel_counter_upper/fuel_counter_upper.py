"""
--- Day 1: The Tyranny of the Rocket Equation ---
https://adventofcode.com/2019/day/1
"""


class FuelCounterUpper:
    """Determines the amount of fuel required to launch"""

    @classmethod
    def calc_fuel_req(cls, mass: int) -> int:
        """calc fuel required for moving input mass
        
        Don't forget to account for the weight of the fuel, too!

        Returns:
            int -- fuel required
        """
        fuel_need = max(int(mass / 3) - 2, 0)

        if fuel_need == 0:
            return 0

        return fuel_need + cls.calc_fuel_req(fuel_need)


if __name__ == "__main__":
    fcu = FuelCounterUpper()

    with open("inputs/day01") as f:
        masses = f.readlines()

    total_fuel = sum([fcu.calc_fuel_req(int(m)) for m in masses])

    print(f"total fuel required = { total_fuel }")
