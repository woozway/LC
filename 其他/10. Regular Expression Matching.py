"""
1. Clarification
2. Possible solutions
    - Recursion
    - Dynamic Programming, top-down
    - Dynamic Programming, bottom-up
3. Coding
4. Tests
"""


# T=O((T+P)*2^(T+P/2)), S=O(T^2 + P^2) required 
# but O((T+P)*2^(T+P/2)) since we're using python3
# T=len(s), P=len(p), 同见 leetcode 44. 通配符匹配
class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p: return True
        if not p: return False
        if not s:
            return self.isMatch(s, p[2:]) if len(p)>=2 and p[1]=='*' else False
        if p[0] == '.' or p[0] == s[0]:
            # 递归的条件就是只要有在前进就好，这样保证不会出现死循环
            return self.isMatch(s[1:], p) or self.isMatch(s, p[2:]) if len(p)>=2 and p[1]=='*' else self.isMatch(s[1:], p[1:])
        else:
            return self.isMatch(s, p[2:]) if len(p)>=2 and p[1]=='*' else False


# T=O(T*P), S=O(T*P), dp[i][j]: Does s[i:] match p[j:]?
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


# T=O(T*P), S=O(T*P)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
