"""
1. Clarification
2. Possible solutions
 - exp and log
 - binary search I
 - Newton's method
3. Coding
4. Tests
"""


# # T=O(1), S=O(1)
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 0: return -1
#         if x == 0: return 0
#         ans = int(math.exp(0.5 * math.log(x)))
#         return ans + 1 if (ans + 1) ** 2 <= x else ans


# T=O(lgx), S=O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0: return -1
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


# # T=O(lgx), S=O(1)
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 0: return -1
#         if x == 0: return 0
#         C, x0 = float(x), float(x)
#         while True:
#             xi = 0.5 * (x0 + C / x0)
#             if abs(x0 - xi) < 1e-7:
#                 break
#             x0 = xi
#         return int(x0)
