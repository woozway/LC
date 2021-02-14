"""
1. Clarification
2. Possible solutions
 - brute force
 - binary search tree
 - bucket sort
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1), Time Limit Exceeded
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         n = len(nums)
#         if n < 2 or t < 0 or k < 0: return False
#         for i in range(n):
#             for j in range(i+1, n):
#                 if abs(nums[i] - nums[j]) <= t and abs(j - i) <= k:
#                     return True
#         return False


# # T=O(nlgk), S=O(k)
# import sortedcontainers
#
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         def floor(n, bst):
#             le = bst.bisect_right(n) - 1
#             return bst[le] if le >= 0 else None
#
#         def ceiling(n, bst):
#             ge = bst.bisect_right(n)
#             return bst[ge] if ge < len(bst) else None
#
#         n = len(nums)
#         if n < 2 or t < 0 or k < 0: return False
#         bst = sortedcontainers.SortedList()
#         for i, n in enumerate(nums):
#             le = floor(n, bst)
#             if le is not None and n <= le + t:
#                 return True
#             ge = ceiling(n, bst)
#             if ge is not None and ge <= n + t:
#                 return True
#             bst.add(n)
#             if len(bst) > k:
#                 bst.remove(nums[i - k])
#         return False


# T=O(n), S=O(k)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        n = len(nums)
        if n < 2 or t < 0 or k < 0: return False
        buckets = {}
        for i, v in enumerate(nums):
            bucketNum, offset = (v // t, 1) if t else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True
            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                del buckets[nums[i - k] // t if t else nums[i - k]]
        return False
