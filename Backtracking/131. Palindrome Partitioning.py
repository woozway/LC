"""
1. Clarification
2. Possible solutions
    - Backtracking with Dynamic Programming
    - Backtracking with Memoization
3. Coding
4. Tests
"""


# T=O(n * 2^n), S=O(n^2), dp[i][j]: whether s[i..j] is a palindrome?
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            for j in range(i, n):
                if dp[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret


# T=O(n * 2^n), S=O(n^2)
from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n, ret, ans = len(s), list(), list()

        @cache
        def isPalindrome(i: int, j: int) -> int:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return ret
