"""
1. Clarification
2. Possible solutions
    - Brute force, recursion
    - dp
3. Coding
4. Tests
"""


# T=O(nk), S=O(k), k is len(coins), dp[i]: min coin num to reach i
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        Max = amount + 1
        dp = [Max] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return -1 if dp[amount] > amount else dp[amount]
