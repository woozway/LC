"""
1. Clarification
2. Possible solutions
    - Expand Around Center
    - Dynamic programming
    - Manacher's Algorithm
3. Coding
4. Tests
"""


# T=O(n^2), S=O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1: return s
        self.ans = ''
        self.s = s
        for i in range(len(s) - 1):
            self.lp(i, i)
            self.lp(i, i + 1)
        return self.ans

    def lp(self, left, right):
        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            left -= 1
            right += 1
        if right - left - 1 > len(self.ans):
            self.ans = self.s[left + 1:right]


# T=O(n^2), S=O(n^2), Time Limit Exceeded
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1: return s
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ''
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans


# T=O(n), S=O(n)
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1: return s
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]
