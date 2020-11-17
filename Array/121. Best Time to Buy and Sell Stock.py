class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price-minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit
