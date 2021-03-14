"""
1. Clarification
2. Possible solutions
     - Brute Force dfs
     - dfs + Memoization
     - 2D Dynamic Programming
     - 1D Dynamic Programming
3. Coding
4. Tests
"""


# # T=O(2^n), S=O(n), Time Limit Exceeded
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums or S > 1000: return 0
#         self.cnt = 0
#         self.nums = nums
#         self.dfs(0, 0, S)
#         return self.cnt

#     def dfs(self, idx, tmpSum, S):
#         if idx == len(self.nums):
#             if tmpSum == S:
#                 self.cnt += 1
#             return
#         self.dfs(idx + 1, tmpSum + self.nums[idx], S)
#         self.dfs(idx + 1, tmpSum - self.nums[idx], S)


# # T=O(n*Sum), S=O(n*Sum), Sum=sum(nums)
# # memo[i][j]: # of possible solutions using nums[i:] and tmpSum j to get to S
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums or S > 1000: return 0
#         self.memo = {i: dict() for i in range(len(nums))}
#         return self.dfs(nums, 0, 0, S)

#     def dfs(self, nums, idx, tmpSum, S):
#         if idx == len(nums): return 1 if tmpSum == S else 0
#         if tmpSum not in self.memo[idx]:
#             self.memo[idx][tmpSum] = self.dfs(nums, idx + 1, tmpSum + nums[idx], S) \
#                                      + self.dfs(nums, idx + 1, tmpSum - nums[idx], S)
#         return self.memo[idx][tmpSum]


# T=O(n*Sum), S=O(n*Sum)
# dp[i][j]: # of solutions using [0...i] elements to get sum j
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums or S > 1000: return 0
        n = len(nums)
        dp = {i: collections.Counter() for i in range(n)}
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1
        for i in range(1, n):
            for j in range(-1000, 1001):
                dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
        return dp[n - 1][S]


# # T=O(n*Sum), S=O(n)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums or S > 1000: return 0
#         dp, next = (collections.Counter() for _ in range(2))
#         dp[nums[0]] += 1
#         dp[-nums[0]] += 1
#         for i in range(1, len(nums)):
#             next.clear()
#             for j in range(-1000, 1001):
#                 next[j + nums[i]] += dp[j]
#                 next[j - nums[i]] += dp[j]
#             dp = next.copy()
#         return dp[S]
