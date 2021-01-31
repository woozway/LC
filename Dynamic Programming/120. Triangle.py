"""
1. Clarification
2. Possible solutions
 - dynamic programming
 - dp + state compression
3. Coding
4. Tests
"""

# # T=O(n^2), S=O(n^2)
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)
#         f = [[0] * n for _ in range(n)]
#         f[0][0] = triangle[0][0]
#         for i in range(1, n):
#             f[i][0] = f[i - 1][0] + triangle[i][0]
#             for j in range(1, i):
#                 f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
#             f[i][i] = f[i - 1][i - 1] + triangle[i][i]
#         return min(f[n - 1])


# T=O(n^2), S=O(n)
class Solution:
    def minimumTotal(self, triangle) -> int:
        if not triangle: return 0
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]
