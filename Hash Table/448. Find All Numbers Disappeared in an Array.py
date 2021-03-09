"""
1. Clarification
2. Possible solutions
     - HashMap
     - In-place
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums: return []
        hash_table = {}
        for num in nums:
            hash_table[num] = 1
        result = []
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
        return result


# # T=O(n), S=O(1)
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         if not nums: return []
#         for i in range(len(nums)):
#             new_index = abs(nums[i]) - 1
#             if nums[new_index] > 0:
#                 nums[new_index] *= -1
#         result = []
#         for i in range(1, len(nums) + 1):
#             if nums[i - 1] > 0:
#                 result.append(i)
#         return result
