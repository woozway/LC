"""
1. Clarification
2. Possible solutions
    - pythonic
    - x & 1 + count + x >> 1
    - Brian Kernighan Algorithm: x & (x - 1) to get the last 1-bit
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
    
    
# # T=O(1), S=O(1)
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         rst, mask = 0, 1
#         for i in range(32):
#             if n & mask:
#                 rst += 1
#             mask <<= 1
#         return rst


# T=O(1), S=O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        rst = 0
        while n:
            n &= n - 1
            rst += 1
        return rst
