"""
1. Clarification
2. Possible solutions
     - recursion, naive fibonacci
     - memoization
     - dynamic programming
     - Fibonacci Formula
3. Coding
4. Tests
"""

# # T=O(2^n), S=O(n), Time Limit Exceeded
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2: return n
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# # T=O(n), S=O(n)
# class Solution:
#     def __init__(self):
#         self.memo = {}
#
#     def climbStairs(self, n: int) -> int:
#         if n <= 2: return n
#         if self.memo.get(n, 0) == 0:
#             self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
#         return self.memo[n]


# T=O(n), S=O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 1, 1
        for _ in range(1, n):
            x, y = y, x + y
        return y


# # T=O(lgn), S=O(1)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         sqrt5 = 5 ** 0.5
#         fibn = math.pow((1 + sqrt5)/2, n + 1) - math.pow((1 - sqrt5)/2, n + 1)
#         return int(fibn / sqrt5)
