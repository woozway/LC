"""
1. Clarification
2. Possible solutions
 - linear scan
 - binary search III
 - python built-in bisect
3. Coding
4. Tests
"""


# # T=O(n), S=O(1)
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums: return [-1, -1]
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 left_idx = i
#                 break
#         else:
#             return [-1, -1]
#         for j in range(len(nums) - 1, -1, -1):
#             if nums[j] == target:
#                 right_idx = j
#                 break
#         return [left_idx, right_idx]


# T=O(lgn), S=O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        left_idx = self.extreme_insertion_index(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]

    def extreme_insertion_index(self, nums, target, left):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo


# # T=O(lgn), S=O(1)
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums: return [-1, -1]
#         left = bisect.bisect_left(nums, target)
#         if left != len(nums) and nums[left] == target:
#             return [left, bisect.bisect(nums, target) - 1]
#         else:
#             return [-1, -1]
