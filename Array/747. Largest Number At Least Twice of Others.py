"""
1. Clarification
2. Possible solutions
 - linear scan
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums: return -1
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1
