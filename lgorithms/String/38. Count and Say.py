"""
1. Clarification
2. Possible solutions
    - String
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n - 1)
        i, j, ans = 0, 1, list()
        while j <= len(s):
            if j == len(s):
                ans.extend([str(j-i), s[i]])
            elif s[i] != s[j]:
                ans.extend([str(j-i), s[i]])
                i = j
            j += 1
        return ''.join(ans)
