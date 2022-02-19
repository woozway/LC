"""
1. Clarification
2. Possible solutions
    - Bit Manipulation
    - Shift
    - Brian Kernighan algorithm
3. Coding
4. Tests
"""


# T=O(1), S=O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


# T=O(1), S=O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s, ret = x ^ y, 0
        while s:
            ret += s & 1
            s >>= 1
        return ret


# T=O(1), S=O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s, ret = x ^ y, 0
        while s:
            s &= s - 1
            ret += 1
        return ret
