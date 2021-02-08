"""
1. Clarification
2. Possible solutions
 - brute force
 - recursive binary search II
 - iterative binary search II
3. Coding
4. Tests
"""


# # T=O(n), S=O(1)
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         if not nums: return -1
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 return i
#         return len(nums) - 1


# T=O(lgn), S=O(lgn)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums: return -1
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums, left, right):
        if left == right: return left
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, left, mid)
        return self.search(nums, mid + 1, right)


# T=O(lgn), S=O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
