"""
1. Clarification
2. Possible solutions
     - hash table
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
