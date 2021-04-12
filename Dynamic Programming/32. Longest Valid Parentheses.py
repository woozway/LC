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


# T=O(n), S=O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        maxAns = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxAns = max(maxAns, i - stack[-1])
        return maxAns


# T=O(n), S=O(1)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        left, right = 0, 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, 2 * left)
            elif left > right:
                left = right = 0
        return maxlen
