"""
1. Clarification
2. Possible solutions
 - brute force, recursion
 - dp
 - binary search
3. Coding
4. Tests
"""


# T=O(n^2), S=O(n), dp[i]: len of LIS when selecting nums[i]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            dp[i] = 1 + max([dp[j] for j in range(i) if nums[j] < nums[i]] + [0])
        return max(dp)


# # T=O(nlgn), S=O(n), binary search
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         lis = []
#         for i in range(len(nums)):
#             p = bisect.bisect_left(lis, nums[i])
#             if p == len(lis):
#                 lis.append(nums[i])
#             else:
#                 lis[p] = nums[i]
#         return len(lis)
