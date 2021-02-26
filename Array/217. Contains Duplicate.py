"""
1. Clarification
2. Possible solutions
     - sort
     - hashset
3. Coding
4. Tests
"""


# # T=O(nlgn), S=O(lgn)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return True
#         return False


# T=O(n), S=O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
