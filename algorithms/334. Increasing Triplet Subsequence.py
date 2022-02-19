"""
1. Clarification
2. Possible solutions
    - Dynamic Programming
    - Greedy
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(n), Time Limit Exceeded
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         return self.longestIncreasingSubSequence(nums) >= 3

#     def longestIncreasingSubSequence(self, nums):
#         n = len(nums)
#         dp = [1] * n
#         for i in range(1, n):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)


# T=O(n), S=O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
