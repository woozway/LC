"""
1. Clarification
2. Possible solutions
    - Sliding window v1
    - Sliding window v2
3. Coding
4. Tests
"""


# T=O(s+t), S=O(s+t)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ''
        dict_t = collections.Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = collections.Counter()
        ans = float('inf'), None, None
        while r < len(s):
            char = s[r]
            window_counts[char] += 1
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            while l <= r and formed == required:
                char = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                l += 1
            r += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]


# T=O(s+t), S=O(s+t)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ''
        dict_t = collections.Counter(t)
        required = len(dict_t)
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))
        l, r = 0, 0
        formed = 0
        window_counts = collections.Counter()
        ans = float('inf'), None, None
        while r < len(filtered_s):
            char = filtered_s[r][1]
            window_counts[char] += 1
            if window_counts[char] == dict_t[char]:
                formed += 1
            while l <= r and formed == required:
                char = filtered_s[l][1]
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                window_counts[char] -= 1
                if window_counts[char] < dict_t[char]:
                    formed -= 1
                l += 1
            r += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
