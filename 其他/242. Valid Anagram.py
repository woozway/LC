"""
1. Clarification
2. Possible solutions
 - sort string s & t
 - hashMap
3. Coding
4. Tests
"""

# # T=O(nlgn)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# T=O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
