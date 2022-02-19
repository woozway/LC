"""
1. Clarification
2. Possible solutions
    - Brute force
    - Dynamic programming
3. Coding
4. Tests
"""


# # T=O(n^(target/min(nums)), Time Limit Exceeded
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         def backtrack(tmpSum):
#             if tmpSum > target: return
#             if tmpSum == target:
#                 ans.add(tuple(tmpList))
#                 return
#             for i in range(n):
#                 tmpList.append(nums[i])
#                 backtrack(tmpSum + nums[i])
#                 tmpList.pop()
#
#         if not nums: return 0
#         n = len(nums)
#         ans, tmpList = set(), list()
#         backtrack(0)
#         return len(ans)


# T=O(target*n), S=O(target)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]
