"""
1. Clarification
2. Possible solutions
 - x & 1 + count + x >> 1
 - Brian Kernighan Algorithm: x & (x - 1)
3. Coding
4. Tests
"""

# # T=O(1), S=O(1)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n:
#             if n & 1:
#                 count += 1
#             n >>= 1
#         return count

# T=O(1), S=O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
