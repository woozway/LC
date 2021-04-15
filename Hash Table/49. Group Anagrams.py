"""
1. Clarification
2. Possible solutions
    - Sort
    - Categorized by Count
3. Coding
4. Tests
"""


# T=O(nklgk), S=O(nk), k=avg length of strs
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


# T=O(nk), S=O(nk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
