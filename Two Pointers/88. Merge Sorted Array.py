"""
1. Clarification
2. Possible solutions
 - brute quicksort
 - two pointers v1
 - two pointers v2
3. Coding
4. Tests
"""


# # T=O((m+n)lg(m+n)), S=O(1)
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         if not nums1 or not nums2: return
#         nums1[:] = sorted(nums1[:m] + nums2)


# # T=O(n+m), S=O(m)
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         if not nums1 or not nums2: return
#         nums1_copy = nums1[:m]
#         nums1[:] = []
#         p1 = 0
#         p2 = 0
#         while p1 < m and p2 < n:
#             if nums1_copy[p1] < nums2[p2]:
#                 nums1.append(nums1_copy[p1])
#                 p1 += 1
#             else:
#                 nums1.append(nums2[p2])
#                 p2 += 1
#         if p1 < m:
#             nums1[p1 + p2:] = nums1_copy[p1:]
#         if p2 < n:
#             nums1[p1 + p2:] = nums2[p2:]


# T=O(n+m), S=O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums1 or not nums2: return
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
