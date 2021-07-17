"""
1. Clarification
2. Possible solutions
    - String
    - Maths
3. Coding
4. Tests
"""


# T=O(lgx), S=O(lgx)
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        s = str(x)
        rev = int(s[::-1])
        return 0 if not (-2**31 <= rev <= 2**31-1) else rev


# T=O(lgx), S=O(1)
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        rev = 0
        while x != 0:
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
        return rev
