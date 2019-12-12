class Password:
    @classmethod
    def count_valid_combos(self, low, high, validator):
        """
        returns the number of possible passwords between [low, high]
        given the reqs above
        """
        valid_count = 0
        for n in range(low, high + 1):
            digits = []
            for m in [100000, 10000, 1000, 100, 10, 1]:
                digits.append(int(n / m % 10))

            if validator(digits):
                valid_count += 1

        return valid_count

    @classmethod
    def validator_1(self, digits):
        """
        validates according to these rules:

        * It is a six-digit number.
        * The value is within the range given in your puzzle input.
        * Two adjacent digits are the same (like 22 in 122345).
        * Going from left to right, the digits never decrease.
        """
        pair_found = False
        for i in range(0, len(digits) - 1):
            if digits[i] > digits[i + 1]:
                return False
            if digits[i] == digits[i + 1]:
                pair_found = True
        return pair_found


if __name__ == "__main__":
    # puzzle input
    low = 130254
    high = 678275

    combos = Password.count_valid_combos(low, high, Password.validator_1)
    print(f"{ combos } possible combos between { low } and { high } inclusive")
