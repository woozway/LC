"""
1. Clarification
2. Possible solutions
 - recursion
 - two pointers
3. Coding
4. Tests
"""


# # T=O(n), S=O(n)
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         def helper(left, right):
#             if left < right:
#                 s[left], s[right] = s[right], s[left]
#                 helper(left + 1, right - 1)
# 
#         if not s: return
#         helper(0, len(s) - 1)


# T=O(n), S=O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        if not s: return
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
