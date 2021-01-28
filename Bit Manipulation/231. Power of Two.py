"""
1. Clarification
2. Possible solutions
 - mod
 - log2
 - bit manipulation (2 versions)
3. Coding
4. Tests
"""

# # T=O(lgn), S=O(1)
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0: return False
#         while n & 1 == 0:
#             n >>= 1
#         return n == 1

# # T=O(1), S=O(1)
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0: return False
#         return math.log2(n) % 1 == 0

# # T=O(1), S=O(1)
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0: return False
#         return n & (-n) == n

# T=O(1), S=O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return (n & (n - 1)) == 0
