"""
1. Clarification
2. Possible solutions
     - Hash table v1
     - Hash table v2
     - Pythonic
3. Coding
4. Tests
"""


# T=O(n), S=O(len(alphabet))
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d = dict()
        S = set()
        for i, x in enumerate(s):
            if d.get(x, 0) == 0:
                d[x] = t[i]
                if t[i] in S:
                    return False
                else:
                    S.add(t[i])
            else:
                if d[x] != t[i]:
                    return False
        return True


# T=O(n), S=O(len(alphabet))
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d1, d2 = {}, {}
        for v, w in zip(s,t):
            if (v in d1 and d1[v] != w) or (w in d2 and d2[w] != v):
                return False
            d1[v], d2[w] = w, v
        return True


# T=O(n), S=O(len(alphabet))
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
