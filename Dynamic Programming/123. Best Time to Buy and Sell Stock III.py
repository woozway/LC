"""
1. Clarification
2. Possible solutions
 - dp1 & dp2
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
# dp[i][j][k], i: day, j: former transaction times, k: whether to buy a stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
        dp[0][0][0], dp[0][0][1] = 0, -prices[0]
        dp[0][1][0], dp[0][1][1] = -inf, -inf
        dp[0][2][0], dp[0][2][1] = -inf, -inf
        for i in range(1, n):
            dp[i][0][0] = dp[i - 1][0][0]
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][0][0] - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][1][0] - prices[i])
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][1][1] + prices[i])
        return max(dp[n-1][0][0], dp[n-1][1][0], dp[n-1][2][0])


# # T=O(n), S=O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         buy1 = buy2 = -prices[0]
#         sell1 = sell2 = 0
#         for i in range(1, n):
#             buy1 = max(buy1, -prices[i])
#             sell1 = max(sell1, buy1 + prices[i])
#             buy2 = max(buy2, sell1 - prices[i])
#             sell2 = max(sell2, buy2 + prices[i])
#         return sell2
