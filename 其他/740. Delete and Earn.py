"""
1. Clarification
2. Possible solutions
    - Dynamic programming v1
    - Dynamic programming v2
3. Coding
4. Tests
"""


# T=O(n+m), S=O(m), m=max(nums), see leetcode 198.
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for val in nums:
            total[val] += val

        def rob(nums: List[int]) -> int:
            size = len(nums)
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, size):
                first, second = second, max(first + nums[i], second)
            return second

        return rob(total)


# T=O(nlgn), S=O(n)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)
