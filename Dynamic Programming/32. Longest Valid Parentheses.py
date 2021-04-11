"""
1. Clarification
2. Possible solutions
    - Dynamic programming
    - Stack
    - Without extra space
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        maxAns = 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0) + 2
                maxAns = max(maxAns, dp[i])
        return maxAns
