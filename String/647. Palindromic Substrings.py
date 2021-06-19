"""
1. Clarification
2. Possible solutions
    - Brute force
    - Inside out
    - Manacher algorithm
3. Coding
4. Tests
"""


# # T=O(n^3), S=O(1), Time Limit Exceeded
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         ans = 0
#         for i in range(1, len(s) + 1):
#             for j in range(len(s) - i + 1):
#                 if self.isPalindrome(s[j:j+i]):
#                     ans += 1
#         return ans
#
#     def isPalindrome(self, s):
#         left, right = 0, len(s)-1
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             else:
#                 left += 1
#                 right -= 1
#         return True


# T=O(n^2), S=O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0
        for i in range(2 * n - 1):
            left, right = i // 2, i // 2 + i % 2
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1
        return ans


# T=O(n), S=O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '$#'
        for ch in s:
            t += ch + '#'
        n = len(t)
        t += '!'
        f, iMax, rMax, ans = [0] * n, 0, 0, 0
        for i in range(1, n):
            f[i] = min(rMax - i + 1, f[2 * iMax - i]) if i <= rMax else 1
            while t[i + f[i]] == t[i - f[i]]:
                f[i] += 1
            if i + f[i] - 1 > rMax:
                iMax = i
                rMax = i + f[i] - 1
            ans += f[i] // 2
        return ans
