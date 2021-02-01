"""
1. Clarification
2. Possible solutions
 - one pass
 - dynamic programming
3. Coding
4. Tests
"""


# # T=O(n), S=O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         inf = int(1e9)
#         minPrice = inf
#         maxProf = 0
#         for price in prices:
#             maxProf = max(price - minPrice, maxProf)
#             minPrice = min(price, minPrice)
#         return maxProf


# T=O(n), S=O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        res = 0
        dp = [[0] * 3 for i in range(len(prices))]
        dp[0][0], dp[0][1], dp[0][2] = 0, -prices[0], 0
        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
            res = max(res, dp[i][0], dp[i][1], dp[i][2])
        return res
