"""
1. Clarification
2. Possible solutions
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(n^2), S=O(n)
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(j*(i-j), j*dp[i-j], dp[i])
        return dp[n]
