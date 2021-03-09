"""
1. Clarification
2. Possible solutions
     - Sort + lambda
     - Two Passes
     - Two pointers + in-place v1
     - Two pointers + in-place v2
3. Coding
4. Tests
"""


# # T=O(nlgn), S=O(n)
# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         if not A: return []
#         A.sort(key = lambda x: x % 2)
#         return A


# # T=O(n), S=O(n)
# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         if not A: return []
#         return ([x for x in A if x % 2 == 0] +
#                 [x for x in A if x % 2 == 1])


# T=O(n), S=O(1)
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A: return []
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] & 1 != 0:
                A[i], A[j] = A[j], A[i]
                j -= 1
            else:
                i += 1
        return A


# # T=O(n), S=O(1)
# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         if not A: return []
#         i, j = 0, len(A) - 1
#         while i < j:
#             if A[i] % 2 > A[j] % 2:
#                 A[i], A[j] = A[j], A[i]
#             if A[i] % 2 == 0: i += 1
#             if A[j] % 2 == 1: j -= 1
#         return A
