# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Example 1

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i, d in reversed(list(enumerate(digits))):
            if d < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


# <-------------------------------------------------->

# Example 2

class Solution2:
    def plusOne2(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            digits[0] = 1
            digits.append(0)
            return digits


# <------------------------------------------------->

# Example 3

class Solution3:
    def plusOne3(self, digits: list[int]) -> list[int]:
        num = int("".join(map(str, digits))) + 1
        return [int(i) for i in str(num)]

# <-------------------------------------------------->
