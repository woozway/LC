"""
1. Clarification
2. Possible solutions
    - Dynamic programming
    - Maths
3. Coding
4. Tests
"""


# T=O(n^2), S=O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[n]


# T=O(n), S=O(1)
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
