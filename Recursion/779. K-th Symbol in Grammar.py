"""
1. Clarification
2. Possible solutions
     - brute force
     - recursion v1
     - recursion v2
     - binary count
3. Coding
4. Tests
"""


# # T=O(2^n), S=O(2^n), Time Limit Exceeded
# class Solution:
#     def kthGrammar(self, N: int, K: int) -> int:
#         lastrow = '0'
#         rows = []
#         while len(rows) < N:
#             lastrow = ''.join('01' if x == '0' else '10'
#                               for x in lastrow)
#             rows.append(lastrow)
#         return int(rows[-1][K - 1])


# T=O(n), S=O(1)
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1: return 0
        return (1 - K % 2) ^ self.kthGrammar(N - 1, (K + 1) // 2)


# # T=O(n), S=O(1)
# class Solution:
#     def kthGrammar(self, N: int, K: int) -> int:
#         if N == 1: return 0
#         if K <= 2 ** (N - 2):
#             return self.kthGrammar(N - 1, K)
#         return self.kthGrammar(N - 1, K - 2 ** (N - 2)) ^ 1


# # T=O(lgn), S=O(1)
# class Solution:
#     def kthGrammar(self, N: int, K: int) -> int:
#         return bin(K - 1).count('1') % 2
