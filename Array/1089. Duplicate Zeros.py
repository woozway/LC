"""
1. Clarification
2. Possible solutions
     - Brute insert 0
     - Two pointers
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
        n = len(arr)
        taken = possible_dups = zero_count = 0
        for num in arr:
            if num != 0:
                taken += 1
            else:
                zero_count += 1
                if n - taken != 1:
                    possible_dups += 1
                taken += 2
            if taken >= n:
                break
        if zero_count != possible_dups:
            arr[n - 1] = 0
        right = n - 1 - possible_dups - (zero_count - possible_dups)
        for i in range(right, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
