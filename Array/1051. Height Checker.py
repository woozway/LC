"""
1. Clarification
2. Possible solutions
     - Sort
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if not heights: return 0
        a = sorted(heights)
        count, n = 0, len(heights)
        for i in range(n):
            if heights[i] != a[i]:
                count += 1
        return count


# # T=O(n), S=O(1)
# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         if not heights: return 0
#         arr = [0] * 101
#         for height in heights:
#             arr[height] += 1
#         count = 0
#         j = 0
#         for i in range(1, 101):
#             while arr[i] > 0:
#                 if heights[j] != i:
#                     count += 1
#                 j += 1
#                 arr[i] -= 1
#         return count
