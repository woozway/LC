"""
1. Clarification
2. Possible solutions
 - library function
 - built-in calculation
 - brute force
 - fast exp, recursive (divide and conquer)
 - fast exp, iterative
3. Coding
4. Tests
"""

# # T=O(1)
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         return pow(x, n)

# # T=O(lgn)
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         return x**n

# # T=O(n), Time Limit Exceeded
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         ans = 1.0
#         flag = True
#         if n < 0:
#             flag = False
#             n = -n
#         for _ in range(n):
#             ans *= x
#         return 1/ans if flag == False else ans

# # T=O(lgn), S=O(lgn)
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if not n: return 1
#         if n < 0: return 1 / self.myPow(x, -n)
#         if n % 2: return x * self.myPow(x, n-1)
#         return self.myPow(x*x, n//2)

# T=O(lgn), S=O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow
