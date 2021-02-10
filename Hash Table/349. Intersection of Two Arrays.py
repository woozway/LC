"""
1. Clarification
2. Possible solutions
 - built-in set intersection
 - set
3. Coding
4. Tests
"""


# T=O(m+n), S=O(m+n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        # return collections.Counter(nums1) & collections.Counter(nums2)
        return set(nums1) & set(nums2)


# # T=O(m+n), S=O(m+n)
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         if not nums1 or not nums2: return []
#         set1 = set(nums1)
#         set2 = set(nums2)
#         if len(set1) < len(set2):
#             return self.set_intersection(set1, set2)
#         else:
#             return self.set_intersection(set2, set1)
#
#     def set_intersection(self, set1, set2):
#         return [x for x in set1 if x in set2]
