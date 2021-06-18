"""
1. Clarification
2. Possible solutions
    - Brute force + sorting
    - Hash
3. Coding
4. Tests
"""


# T=O(ns * np * lg(np)), S=O(np)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        ns, np = len(s), len(p)
        pInOrder = sorted(p)
        ans = list()
        for i in range(ns - np + 1):
            if sorted(s[i:i+np]) == pInOrder:
                ans.append(i)
        return ans


# T=O(ns * len(keys in pCounter)), S=O(np)
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        ns, np = len(s), len(p)
        pCounter, runningCounter = Counter(p), Counter()
        ans = list()
        for i, ch in enumerate(s):
            if i < np:
                runningCounter[ch] += 1
                if i == np - 1 and runningCounter == pCounter:
                    ans.append(i - np + 1)
            else:
                preCh = s[i-np]
                runningCounter[ch] += 1
                runningCounter[preCh] -= 1
                if runningCounter[preCh] == 0:
                    del runningCounter[preCh]
                if runningCounter == pCounter:
                    ans.append(i - np + 1)
        return ans
