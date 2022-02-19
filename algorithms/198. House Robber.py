"""
1. Clarification
2. Possible solutions
    - Dynamic programming v1
    - Dynamic programming v2
3. Coding
4. Tests
"""


# T=O(n), S=O(n), dp[i]: max amount of money when reaching index i in list nums
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


# T=O(n), S=O(1), see also leetcode 740.
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)
        return second
