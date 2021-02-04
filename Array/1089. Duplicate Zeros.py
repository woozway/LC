"""
1. Clarification
2. Possible solutions
 - brute force
 - two passes
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1)
# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         if not arr: return
#         n, i = len(arr), 0
#         while i < n:
#             if arr[i] != 0:
#                 i += 1
#             else:
#                 for j in range(n - 2, i - 1, -1):
#                     arr[j + 1] = arr[j]
#                 i += 2


# T=O(n), S=O(1)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        if not arr: return
        possible_dups = 0
        length_ = len(arr) - 1
        for left in range(length_ + 1):
            if left > length_ - possible_dups:
                break
            if arr[left] == 0:
                if left == length_ - possible_dups:
                    arr[length_] = 0
                    length_ -= 1
                    break
                possible_dups += 1
        last = length_ - possible_dups
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
