"""
1. Clarification
2. Possible solutions
 - binary search
 - Newton's iterative method
3. Coding
4. Tests
"""

# T=O(lgx), S=O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
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
#         r = x
#         while r * r > x:
#             r = (r + x // r) // 2
#         return r
