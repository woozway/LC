"""
1. Clarification
2. Possible solutions
    - Dynamic programming v1
    - Dynamic programming v2
    - Dynamic programming v3
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxList, minList = nums[:], nums[:]
        for i in range(1, len(nums)):
            maxList[i] = max(maxList[i-1] * nums[i], nums[i], minList[i-1] * nums[i])
            minList[i] = min(maxList[i-1] * nums[i], nums[i], minList[i-1] * nums[i])
        return max(maxList)


# T=O(n), S=O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None: return 0
        dp = [[0] * 2 for _ in range(2)]
        dp[0][0] = dp[0][1] = res = nums[0]
        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])
        return res


# T=O(n), S=O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None: return 0
        res, curMax, curMin = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curMax, curMin = curMax * num, curMin * num
            curMin, curMax = min(curMax, curMin, num), max(curMax, curMin, num)
            res = curMax if curMax > res else res
        return res
