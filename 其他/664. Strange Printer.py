"""
1. Clarification
2. Possible solutions
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(n^3), S=O(n^2), dp[i][j]: # min ops to finish string in range [i..j]
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    minn = math.inf
                    for k in range(i, j):
                        minn = min(minn, dp[i][k] + dp[k + 1][j])
                    dp[i][j] = minn
        return dp[0][-1]
