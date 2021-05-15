"""
1. Clarification
2. Possible solutions
    - dp
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
# dp[i][j], i: day, j:
#         0 - have a share of stock
#         1 - have no stock and cool down next day
#         2 - have no stock and no cool down next day
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0], dp[0][1], dp[0][2] = -prices[0], 0, 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[n - 1][1], dp[n - 1][2])
