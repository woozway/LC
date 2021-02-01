"""
1. Clarification
2. Possible solutions
 - dp
3. Coding
4. Tests
"""


# T=O(nk), S=O(nk)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        for i in range(k + 1):
            dp[0][i][0], dp[0][i][1] = 0, -prices[0]
        for i in range(1, n):
            for j in range(0, k + 1):
                if j == 0:
                    dp[i][0][0] = dp[i - 1][0][0]
                    dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][0][0] - prices[i])
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])
        maxProf = 0
        for i in range(k + 1):
            maxProf = max(maxProf, dp[n - 1][i][0])
        return maxProf
