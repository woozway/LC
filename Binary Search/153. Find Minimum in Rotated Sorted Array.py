"""
1. Clarification
2. Possible solutions
 - way too clever
 - binary search II
3. Coding
4. Tests
"""


# # T=O(n), S=O(1)
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         if not nums: return int(-inf)
#         return min(nums)


# T=O(lgn), S=O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return int(-inf)
        left, right = 0, len(nums) - 1
        while nums[left] > nums[right]:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
