"""
1. Clarification
2. Possible solutions
 - brute quicksort
 - two pointers v1
 - two pointers v2
3. Coding
4. Tests
"""


# # T=O(nlgn), S=O(lgn)
# class Solution:
#     def sortedSquares(self, A: List[int]) -> List[int]:
#         if not A: return []
#         return sorted(num * num for num in A)


# # T=O(n), S=O(1)
# class Solution:
#     def sortedSquares(self, A: List[int]) -> List[int]:
#         if not A: return []
#         n = len(A)
#         negative = -1
#         for i, num in enumerate(A):
#             if num < 0:
#                 negative = i
#             else:
#                 break
#         ans = list()
#         i, j = negative, negative + 1
#         while i >= 0 or j < n:
#             if i < 0:
#                 ans.append(A[j] * A[j])
#                 j += 1
#             elif j == n:
#                 ans.append(A[i] * A[i])
#                 i -= 1
#             elif A[i] * A[i] < A[j] * A[j]:
#                 ans.append(A[i] * A[i])
#                 i -= 1
#             else:
#                 ans.append(A[j] * A[j])
#                 j += 1
#         return ans


# T=O(n), S=O(1)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A: return []
        n = len(A)
        ans = [0] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                ans[pos] = A[i] * A[i]
                i += 1
            else:
                ans[pos] = A[j] * A[j]
                j -= 1
            pos -= 1
        return ans
