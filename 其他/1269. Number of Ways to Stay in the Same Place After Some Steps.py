"""
1. Clarification
2. Possible solutions
    - Dynamic programming v1
    - Dynamic programming v2
3. Coding
4. Tests
"""


# T=O(steps * min(arrLen, steps)), S=O(steps * min(arrLen, steps))
# dp[i][j]: after i steps, number of ways to stay at index j
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if steps < 1 or arrLen < 1: return 0
        mod = 10 ** 9 + 7
        maxColumn = min(arrLen - 1, steps)
        dp = [[0] * (maxColumn + 1) for _ in range(steps + 1)]
        dp[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(0, maxColumn + 1):
                dp[i][j] = dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                if j + 1 <= maxColumn:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
        return dp[steps][0]


# T=O(steps * min(arrLen, steps)), S=O(min(arrLen, steps))
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if steps < 1 or arrLen < 1: return 0
        mod = 10 ** 9 + 7
        maxColumn = min(arrLen - 1, steps)
        dp = [0] * (maxColumn + 1)
        dp[0] = 1
        for i in range(1, steps + 1):
            dpNext = [0] * (maxColumn + 1)
            for j in range(0, maxColumn + 1):
                dpNext[j] = dp[j]
                if j - 1 >= 0:
                    dpNext[j] = (dpNext[j] + dp[j - 1]) % mod
                if j + 1 <= maxColumn:
                    dpNext[j] = (dpNext[j] + dp[j + 1]) % mod
            dp = dpNext
        return dp[0]
