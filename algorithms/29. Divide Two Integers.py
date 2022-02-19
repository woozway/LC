"""
1. Clarification
2. Possible solutions
    - Cheating
    - Natural
3. Coding
4. Tests
"""


# # T=O(1), S=O(1)
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         x = int(dividend / divisor)
#         return x if -2**31 <= x <= 2**31 - 1 else 2**31-1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def div(a, b):
            if a < b: return 0
            count, tmp = 1, b
            while 2 * tmp <= a:
                count *= 2
                tmp *= 2
            return count + div(a - tmp, b)

        intMin, intMax = -2**31, 2**31-1
        if dividend == 0: return 0
        if divisor == 1: return dividend
        if divisor == -1:
            if dividend > intMin: return -dividend
            return intMax
        a, b, sign = dividend, divisor, 1
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            sign = -1
        a, b = abs(a), abs(b)
        res = div(a, b)
        if sign > 0: return intMax if res > intMax else res
        return -res
