"""
1. Clarification
2. Possible solutions
    - Greedy
3. Coding
4. Tests
"""


# T=O(n), S=O(len(alphabet))
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i, ch in enumerate(s):
            dic[ch] = i
        left, right = 0, dic[s[0]]
        res = []
        for i, ch in enumerate(s):
            right = max(right, dic[ch])
            if i >= right:
                res.append(right - left + 1)
                left = right + 1
        return res
