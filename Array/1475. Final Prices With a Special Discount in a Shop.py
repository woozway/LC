class Solution:
  def finalPrices(self, prices: List[int]) -> List[int]:
    """
    T=O(n), monotone stack
    """
    n = len(prices)
    stack = []
    ans = prices[:]
    for i in range(n):
      while stack and prices[i] <= prices[stack[-1]]:
        ans[stack.pop()] -= prices[i]
      stack.append(i)
    return ans
