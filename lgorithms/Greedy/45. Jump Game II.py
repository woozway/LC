"""
1. Clarification
2. Possible solutions
    - Dynamic programming
    - Greedy v1
    - Greedy v2
3. Coding
4. Tests
"""


# T=O(n*max(nums)), S=O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] + [n] * (n - 1)
        for i in range(n):
            for j in range(i + 1, i + nums[i] + 1):
                if j < n:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]


# T=O(n^2), S=O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        pos, step = len(nums) - 1, 0
        while pos > 0:
            for i in range(pos):
                if i + nums[i] >= pos:
                    pos = i
                    step += 1
                    break
        return step


# T=O(n), S=O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
