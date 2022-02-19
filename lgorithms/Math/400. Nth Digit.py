"""
1. Clarification
2. Possible solutions
     - Maths
3. Coding
4. Tests
"""


# T=O(lgn), S=O(1)
class Solution:
    def findNthDigit(self, n: int) -> int:
        base, digit, num = 9, 1, 0
        while n > base*digit:
            n -= base*digit
            num += base
            base *= 10
            digit += 1
        num += (n-1)//digit + 1
        index = (n-1)%digit + 1
        while digit > index:
            num //= 10
            digit -= 1
        return num % 10
