"""
1. Clarification
2. Possible solutions
    - Dynamic programming
    - Maths
3. Coding
4. Tests
"""


# T=O(m*n), S=O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1: return 0
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# T=O(min(m,n)), S=O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1: return 0
        return math.comb(m + n - 2, n - 1)
