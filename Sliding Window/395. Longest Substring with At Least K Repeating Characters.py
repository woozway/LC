"""
1. Clarification
2. Possible solutions
    - Brute force
    - Divide and Conquer
    - Sliding window
3. Coding
4. Tests
"""


# T=O(n^2), S=O(1)
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n < k:
            return 0
        ret = 0
        for start in range(n):
            countMap = Counter()
            for end in range(start, n):
                countMap[ord(s[end]) - ord('a')] += 1
                if self.isValid(s, start, end, k, countMap):
                    ret = max(ret, end - start + 1)
        return ret

    def isValid(self, s, start, end, k, countMap):
        countLetters, countAtLeastK = 0, 0
        for i in range(26):
            if countMap[i] > 0:
                countLetters += 1
            if countMap[i] >= k:
                countAtLeastK += 1
        return countAtLeastK == countLetters


# T=O(n^2), S=O(n)
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.longestSubstringUtil(s, 0, len(s), k)

    def longestSubstringUtil(self, s, start, end, k):
        if end < k: return 0
        countMap = Counter()
        for i in range(start, end):
            countMap[ord(s[i]) - ord('a')] += 1
        for mid in range(start, end):
            if countMap[ord(s[mid]) - ord('a')] >= k:
                continue
            midNext = mid + 1
            while midNext < end and countMap[ord(s[midNext]) - ord('a')] < k:
                midNext += 1
            return max(self.longestSubstringUtil(s, start, mid, k), self.longestSubstringUtil(s, midNext, end, k))
        return end - start


# T=O(n), S=O(1)
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxUnique = self.getMaxUniqueLetters(s)
        ret = 0
        for currUnique in range(1, maxUnique + 1):
            countMap = Counter()
            windowStart, windowEnd, idx, unique, countAtLeastK = 0, 0, 0, 0, 0
            while windowEnd < len(s):
                if unique <= currUnique:
                    idx = ord(s[windowEnd]) - ord('a')
                    if countMap[idx] == 0: unique += 1
                    countMap[idx] += 1
                    if countMap[idx] == k: countAtLeastK += 1
                    windowEnd += 1
                else:
                    idx = ord(s[windowStart]) - ord('a')
                    if countMap[idx] == k: countAtLeastK -= 1
                    countMap[idx] -= 1
                    if countMap[idx] == 0: unique -= 1
                    windowStart += 1
                if unique == currUnique and unique == countAtLeastK:
                    ret = max(ret, windowEnd - windowStart)
        return ret

    def getMaxUniqueLetters(self, s):
        mp, maxUnique = Counter(), 0
        for i in range(len(s)):
            if mp[ord(s[i]) - ord('a')] == 0:
                maxUnique += 1
                mp[ord(s[i]) - ord('a')] = 1
        return maxUnique
