"""
1. Clarification
2. Possible solutions
    - Memoization
    - Dynamic programming
3. Coding
4. Tests
"""


# # T=O(n^3), S=O(n^2), Time Limit Exceeded
# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         n = len(nums)
#         val = [1] + nums + [1]

#         @functools.lru_cache(None)
#         def solve(left: int, right: int) -> int:
#             if left >= right - 1:
#                 return 0
#             best = 0
#             for i in range(left + 1, right):
#                 total = val[left] * val[i] * val[right]
#                 total += solve(left, i) + solve(i, right)
#                 best = max(best, total)
#             return best

#         return solve(0, n + 1)


# T=O(n^3), S=O(n^2)
# dp[i][j]: max # of coins one can get for filling in range (i, j)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
        return dp[0][n + 1]
