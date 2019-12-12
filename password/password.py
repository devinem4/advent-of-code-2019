class Password:
    @classmethod
    def count_valid_combos(self, low, high, validator):
        """
        returns the number of possible passwords between [low, high]
        given the reqs above
        """
        valid_count = 0
        for _ in range(low, high + 1):
            digits = reversed([int(i) for i in str(digits)])

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

    @classmethod
    def validator_2(self, digits):
        """
        same as validator 1 except...

        two adjacent matching digits can not be part of a larger group of 
        matching digits
        """
        for i in range(0, len(digits) - 1):
            if digits[i] > digits[i + 1]:
                return False

        for d in digits:
            if digits.count(d) == 2:
                return True


if __name__ == "__main__":
    # puzzle input
    low = 130254
    high = 678275

    combos = Password.count_valid_combos(low, high, Password.validator_2)
    print(f"{ combos } possible combos between { low } and { high } inclusive")
