"""
1. Clarification
2. Possible solutions
    - Dynamic programming
    - Divide and Conquer
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        maxn, subSum = -math.inf, 0
        for num in nums:
            subSum += num
            maxn = max(maxn, subSum)
            if subSum < 0:
                subSum = 0
        return maxn


# T=O(n), S=O(lgn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_and_conquer(nums, left, right):
            if left == right: return (nums[left], nums[left], nums[left], nums[left])
            mid = (left + right) >> 1
            a1, m1, b1, s1 = divide_and_conquer(nums, left, mid)
            a2, m2, b2, s2 = divide_and_conquer(nums, mid + 1, right)
            a = max(a1, s1 + a2)
            b = max(b2, s2 + b1)
            m = max(m1, m2, b1 + a2)
            s = s1 + s2
            return (a, m, b, s)

        if not nums: return 0
        _, m, _, _ = divide_and_conquer(nums, 0, len(nums) - 1)
        return m
