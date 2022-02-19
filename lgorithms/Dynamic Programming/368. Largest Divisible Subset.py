"""
1. Clarification
2. Possible solutions
    - Brute force + backtracking
    - Dynamic programming
3. Coding
4. Tests
"""


# # T=O(2^n), S=O(2^n), Time Limit Exceeded
# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         if not nums: return []
#         self.ans = []
#         self.tmp = []
#         nums.sort()
#         self.backtrack(nums, 0)
#         return self.ans

#     def backtrack(self, nums, idx):
#         if idx == len(nums):
#             if len(self.tmp) > len(self.ans):
#                 self.ans = self.tmp[:]
#             return
#         if self.tmp and nums[idx] % self.tmp[-1] != 0:
#             self.backtrack(nums, idx + 1)
#         else:
#             self.tmp.append(nums[idx])
#             self.backtrack(nums, idx + 1)
#             self.tmp.pop()
#             self.backtrack(nums, idx + 1)


# T=O(n^2), S=O(n)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1: return nums
        nums.sort()
        n = len(nums)
        dp = [[num] for num in nums]
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + [nums[i]], key=len)
        return max(dp, key=len)
