"""
1. Clarification
2. Possible solutions
  - brute-force
  - use set
3. Coding
4. Tests
"""
# # T=O(n^2), S=O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# T=O(n), S=O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [hash_map[target - x], i]
            hash_map[x] = i
