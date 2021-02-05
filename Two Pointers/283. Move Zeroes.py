"""
1. Clarification
2. Possible solutions
 - two pointers
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums: return
        i, j, n = 0, 0, len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for k in range(j, n):
            nums[k] = 0
