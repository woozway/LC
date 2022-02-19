"""
1. Clarification
2. Possible solutions
    - Dynamic programming v1
    - Dynamic programming v2
3. Coding
4. Tests
"""


# T=O(n*target), S=O(n*target), dp[i][j]: select item(s) from [0..i] to reach value j
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2: return False
        total = sum(nums)
        if total & 1: return False
        maxNum = max(nums)
        target = total // 2
        if maxNum > target: return False
        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(1, target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]


# T=O(n*target), S=O(target)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        return dp[target]
