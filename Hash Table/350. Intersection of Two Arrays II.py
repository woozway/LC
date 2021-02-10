"""
1. Clarification
2. Possible solutions
 - built-in set intersection
3. Coding
4. Tests
"""


# T=O(m+n), S=O(m+n)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        return (collections.Counter(nums1) & collections.Counter(nums2)).elements()
