"""
1. Clarification
2. Possible solutions
 - brute force, dfs
 - greedy algo
 - dp
3. Coding
4. Tests
"""

# # T=O(2^n), S=O(n), Time Limit Exceeded
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         return self.calculate(prices, 0)
#
#     def calculate(self, prices, index):
#         if index >= len(prices): return 0
#         maxn = 0
#         for i in range(index, len(prices)):
#             maxprofit = 0
#             for j in range(i+1, len(prices)):
#                 if prices[i] < prices[j]:
#                     profit = self.calculate(prices, j+1) + (prices[j] - prices[i])
#                     maxprofit = max(maxprofit, profit)
#                 maxn = max(maxn, maxprofit)
#         return maxn

# T=O(n), S=O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

# # T=O(n), S=O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         cur_hold, cur_not_hold = -inf, 0
#         for stock_price in prices:
#             prev_hold, prev_not_hold = cur_hold, cur_not_hold
#             cur_hold = max(prev_hold, prev_not_hold - stock_price)
#             cur_not_hold = max(prev_not_hold, prev_hold + stock_price)   
#         return cur_not_hold
