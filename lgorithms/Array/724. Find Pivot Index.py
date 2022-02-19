"""
1. Clarification
2. Possible solutions
     - Brute force
     - Prefix sum
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1)
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         if not nums: return -1
#         for i in range(len(nums)):
#             if sum(nums[:i]) == sum(nums[i+1:]):
#                 return i
#         return -1


# T=O(n), S=O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums: return -1
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
