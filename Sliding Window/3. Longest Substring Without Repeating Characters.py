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
                curLen = i - j
                while start <= j:
                    del hashMap[s[start]]
                    start += 1
            hashMap[c] = i
            maxLen = max(maxLen, curLen)
        return maxLen


# T=O(n), S=O(len(alphabet))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        window_left, ans = 0, 0
        for i, c in enumerate(s):
            if c in hashMap:
                window_left = max(hashMap[c], window_left)
            ans = max(ans, i - window_left + 1)
            hashMap[c] = i + 1
        return ans
