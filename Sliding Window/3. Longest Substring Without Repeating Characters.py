"""
1. Clarification
2. Possible solutions
    - Sliding window v1
    - Sliding window v2
3. Coding
4. Tests
"""


# T=O(n), S=O(len(alphabet))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        hashMap = {}
        maxLen, curLen, start = 1, 0, 0
        for i, c in enumerate(s):
            if c not in hashMap:
                curLen += 1
            else:
                j = hashMap[c]
                while start <= j:
                    del hashMap[s[start]]
                    start += 1
                curLen = i - j
            hashMap[c] = i
            maxLen = max(maxLen, curLen)
        return maxLen


# T=O(n), S=O(len(alphabet))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans
