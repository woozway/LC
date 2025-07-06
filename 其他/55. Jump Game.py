"""
1. Clarification
2. Possible solutions
    - Going Forwards
    - Going Backwards
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        maxIndex = 0
        for i, num in enumerate(nums):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, i + num)
        return True


# T=O(n), S=O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal
