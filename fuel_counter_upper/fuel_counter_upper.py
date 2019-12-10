"""
--- Day 1: The Tyranny of the Rocket Equation ---
https://adventofcode.com/2019/day/1
"""


class FuelCounterUpper:
    """Determines the amount of fuel required to launch"""

    @classmethod
    def calc_fuel_req(cls, mass: int) -> int:
        """calc fuel required for moving input mass

        Returns:
            int -- fuel required
        """
        return max(int(mass / 3) - 2, 0)
