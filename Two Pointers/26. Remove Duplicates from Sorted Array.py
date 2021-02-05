"""
1. Clarification
2. Possible solutions
 - two pointers
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
