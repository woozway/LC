"""
1. Clarification
2. Possible solutions
 - dp
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
# dp[i][j]: i: day; j:
#         0 - hold no stock
#         1 - hold a stock
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0], dp[0][1] = 0, -prices[0]
        res = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return max(dp[n-1][0], dp[n-1][1])
