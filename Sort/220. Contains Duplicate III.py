"""
1. Clarification
2. Possible solutions
    - Brute force
    - Binary search tree
    - Bucket sort
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1), Time Limit Exceeded
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         n = len(nums)
#         if n < 2 or t < 0 or k < 0: return False
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if abs(nums[i] - nums[j]) <= t and abs(j - i) <= k:
#                     return True
#         return False


# T=O(nlgk), S=O(k)
from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if n < 2 or t < 0 or k < 0: return False
        sList = SortedList()
        for i in range(n):
            if i > k: sList.remove(nums[i - k - 1])   
            pos1 = SortedList.bisect_left(sList, nums[i] - t)
            pos2 = SortedList.bisect_right(sList, nums[i] + t)
            if pos1 != pos2 and pos1 != len(sList):
                return True
            sList.add(nums[i])
        return False


# T=O(n), S=O(k)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        if n < 2 or t < 0 or k < 0: return False
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] // w]
        return False
