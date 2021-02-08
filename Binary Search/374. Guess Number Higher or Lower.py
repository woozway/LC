"""
1. Clarification
2. Possible solutions
 - brute force
 - binary search
 - ternary search
3. Coding
4. Tests
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# # T=O(n), S=O(1), Time Limit Exceeded
# class Solution:
#     def guessNumber(self, n: int) -> int:
#         if n < 1: return 0
#         for i in range(1, n + 1):
#             if guess(i) == 0:
#                 return i
#         return 0


# T=O(lgn), S=O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        if n < 1: return 0
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            ret = guess(mid)
            if ret == 0:
                return mid
            elif ret < 0:
                right = mid - 1
            else:
                left = mid + 1
        return 0


# # T=O(lgn), S=O(1)
# class Solution:
#     def guessNumber(self, n: int) -> int:
#         if n < 1: return 0
#         left, right = 1, n
#         while left <= right:
#             mid1 = left + (right - left) // 3
#             mid2 = right - (right - left) // 3
#             res1 = guess(mid1)
#             res2 = guess(mid2)
#             if res1 == 0:
#                 return mid1
#             if res2 == 0:
#                 return mid2
#             elif res1 < 0:
#                 right = mid1 - 1
#             elif res2 > 0:
#                 left = mid2 + 1
#             else:
#                 left, right = mid1 + 1, mid2 - 1
#         return -1
