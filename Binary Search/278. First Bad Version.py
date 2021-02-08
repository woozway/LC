"""
1. Clarification
2. Possible solutions
 - brute force
 - binary search II
3. Coding
4. Tests
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


# # T=O(n), S=O(1), Time Limit Exceeded
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         if n < 1: return 0
#         for i in range(1, n + 1):
#             if isBadVersion(i):
#                 return i
#         return n + 1


# T=O(lgn), S=O(1)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n < 1: return 0
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
