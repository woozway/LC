"""
1. Clarification
2. Possible solutions
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(mn), S=O(mn), see also leetcode 221.
# dp[i][j]: max side length of with i,j as the right-down index of a square
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if m < 1 or n < 1: return 0
        dp = [[0] * n for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    cnt += dp[i][j]
        return cnt
