"""
1. Clarification
2. Possible solutions
 - bit manipulation
 - dynamic programming
3. Coding
4. Tests
"""

# T=O(nk), S=O(n)
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            res.append(self.bin_count(i))
        return res

    def bin_count(self, n):
        rst = 0
        while n:
            n &= n - 1
            rst += 1
        return rst

# # T=O(n), S=O(n)
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         dp = [0] * (num + 1)
#         for i in range(1, num + 1):
#             dp[i] = dp[i & (i - 1)] + 1
#         return dp
