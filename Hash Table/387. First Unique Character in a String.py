"""
1. Clarification
2. Possible solutions
     - HashMap
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
