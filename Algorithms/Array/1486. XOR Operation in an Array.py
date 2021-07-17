"""
1. Clarification
2. Possible solutions
    - Simulation
    - Maths
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= (start + i * 2)
        return ans


# T=O(1), S=O(1)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s = start >> 1
        e = n & start & 1
        ret = self.sumXor(s - 1) ^ self.sumXor(s + n - 1)
        return ret << 1 | e

    def sumXor(self, x):
        if x % 4 == 0:
            return x
        if x % 4 == 1:
            return 1
        if x % 4 == 2:
            return x + 1
        return 0
