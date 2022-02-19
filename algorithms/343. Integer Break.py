"""
1. Clarification
2. Possible solutions
    - Dynamic programming v1
    - Dynamic programming v2
    - Maths
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


# # T=O(n), S=O(n)
# class Solution:
#     def integerBreak(self, n: int) -> int:
#         if n < 4:
#             return n - 1
        
#         dp = [0] * (n + 1)
#         dp[2] = 1
#         for i in range(3, n + 1):
#             dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])
        
#         return dp[n]


# T=O(1), S=O(1)
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        quotient, remainder = n // 3, n % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2
