"""
1. Clarification
2. Possible solutions
    - Brute force
    - Sorting
    - Stack
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1), Time Limit Exceeded
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         n = len(nums)
#         left, right = n, 0
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if nums[j] < nums[i]:
#                     right, left = max(right, j), min(left, i)
#         return 0 if right - left < 0 else right - left + 1


# T=O(nlgn), S=O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        n = len(nums)
        left, right = n, -1
        for i in range(n):
            if nums_sorted[i] != nums[i]:
                left, right = min(left, i), max(right, i)
        return 0 if left == n and right == -1 else right - left + 1


# T=O(n), S=O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = list()
        n = len(nums)
        left, right = n, -1
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)
        return 0 if left == n and right == -1 else right - left + 1
