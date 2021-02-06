"""
1. Clarification
2. Possible solutions
 - horizontal scanning
 - vertical scanning
 - divide and conquer
 - binary search
3. Coding
4. Tests
"""


# T=O(m*n), S=O(1), m=avg(map(len, strs)), n=len(strs)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]


# # T=O(m*n), S=O(1), m=avg(map(len, strs)), n=len(strs)
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs: return ''
#         if len(strs) == 1: return strs[0]
#         length, count = len(strs[0]), len(strs)
#         for i in range(length):
#             c = strs[0][i]
#             if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
#                 return strs[0][:i]
#         return strs[0]


# # T=O(m*n), S=O(mlgn), m=avg(map(len, strs)), n=len(strs)
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         def lcp(start, end):
#             if start == end: return strs[start]
#             mid = (start + end) // 2
#             lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
#             minLength = min(len(lcpLeft), len(lcpRight))
#             for i in range(minLength):
#                 if lcpLeft[i] != lcpRight[i]:
#                     return lcpLeft[:i]
#             return lcpLeft[:minLength]
#
#         if not strs: return ''
#         if len(strs) == 1: return strs[0]
#         return lcp(0, len(strs) - 1)


# # T=O(mnlogm), S=O(1), m=min(map(len, strs)), n=len(strs)
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         def isCommonPrefix(length):
#             str0, count = strs[0][:length], len(strs)
#             return all(strs[i][:length] == str0 for i in range(1, count))
# 
#         if not strs: return ''
#         if len(strs) == 1: return strs[0]
#         minLength = min(len(s) for s in strs)
#         low, high = 0, minLength
#         while low < high:
#             mid = (high - low + 1) // 2 + low
#             if isCommonPrefix(mid):
#                 low = mid
#             else:
#                 high = mid - 1
#         return strs[0][:low]
