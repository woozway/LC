"""
1. Clarification
2. Possible solutions
    - Mask
    - Mod
3. Coding
4. Tests
"""


# T=O(1), S=O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0


# T=O(1), S=O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
