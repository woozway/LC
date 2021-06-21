"""
1. Clarification
2. Possible solutions
    - Maths
3. Coding
4. Tests
"""


# T=O(lgn), S=O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count
