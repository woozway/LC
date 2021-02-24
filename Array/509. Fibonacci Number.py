"""
1. Clarification
2. Possible solutions
     - Recursion
     - Bottom-Up Approach using Memoization
     - Top-Down Approach using Memoization
     - Iterative Bottom-Up Approach
     - Matrix Exponentiation
     - Math
3. Coding
4. Tests
"""


# # T=O(2^n), S=O(n)
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
#         return self.fib(n - 1) + self.fib(n - 2)


# # T=O(n), S=O(n)
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1: return n
#         return self.memoize(n)

#     def memoize(self, n: int) -> {}:
#         cache = {0: 0, 1: 1}
#         for i in range(2, n + 1):
#             cache[i] = cache[i - 1] + cache[i - 2]
#         return cache[n]


# # T=O(n), S=O(n)
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1: return n
#         self.cache = {0: 0, 1: 1}
#         return self.memoize(n)

#     def memoize(self, n: int) -> {}:
#         if n in self.cache.keys(): return self.cache[n]
#         self.cache[n] = self.memoize(n - 1) + self.memoize(n - 2)
#         return self.memoize(n)


# T=O(n), S=O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        if n == 2: return 1
        current = 0
        prev1 = 1
        prev2 = 1
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current


# # T=O(lgn), S=O(lgn)
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1: return n
#         A = [[1, 1], [1, 0]]
#         self.matrix_power(A, n - 1)
#         return A[0][0]

#     def matrix_power(self, A: list, n: int):
#         if n <= 1: return A
#         self.matrix_power(A, n // 2)
#         self.multiply(A, A)
#         B = [[1, 1], [1, 0]]
#         if n % 2 != 0:
#             self.multiply(A, B)

#     def multiply(self, A: list, B: list):
#         x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
#         y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
#         z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
#         w = A[1][0] * B[0][1] + A[1][1] * B[1][1]
#         A[0][0] = x
#         A[0][1] = y
#         A[1][0] = z
#         A[1][1] = w


# # T=O(1), S=O(1)
# class Solution:
#     def fib(self, n):
#         golden_ratio = (1 + 5 ** 0.5) / 2
#         return int((golden_ratio ** n + 1) / 5 ** 0.5)
