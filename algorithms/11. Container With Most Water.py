"""
1. Clarification
2. Possible solutions
    - Brute force
    - Two pointers
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1), Time Limit Exceeded
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         if n < 2: return 0
#         ans = 0
#         for i in range(n):
#             for j in range(i + 1, n):
#                 ans = max(ans, (j - i) * min(height[i], height[j]))
#         return ans


# T=O(n), S=O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n < 2: return 0
        l, r = 0, n - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
