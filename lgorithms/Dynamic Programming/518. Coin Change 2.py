"""
1. Clarification
2. Possible solutions
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(amount * n), S=O(amount), dp[i]: # ways to represent amount i
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
