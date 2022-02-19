"""
1. Clarification
2. Possible solutions
    - Bit Manipulation, Maths
3. Coding
4. Tests
"""


# T=O(1), S=O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a & mask if b > mask else a
