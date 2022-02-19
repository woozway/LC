"""
1. Clarification
2. Possible solutions
    - Maths
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0
