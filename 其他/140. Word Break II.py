"""
1. Clarification
2. Possible solutions
    - Backtracking, Memoization
3. Coding
4. Tests
"""


# T=O(n * 2^n), S=O(n * 2^n)
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        m = dict()
        st = set(wordDict)

        @lru_cache(None)
        def backtrack(s, index):
            if s in m:
                return
            if index == len(s):
                m[index] = ['']
                return
            m[index] = []
            for i in range(index+1, len(s)+1):
                w = s[index:i]
                if w in st:
                    backtrack(s, i)
                    for j in m[i]:
                        m[index].append(w if not j else w + ' ' + j)

        backtrack(s, 0)
        return m[0]
