class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        monotone stack
        """
        n = len(prices)
        stack = []
        ans = prices[:]
        for i in range(n):
            while True:
                if not stack or prices[i] > prices[stack[-1]]:
                    stack.append(i)
                    break
                else:
                    ans[stack.pop()] -= prices[i]
        return ans
