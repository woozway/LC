"""
1. Clarification
2. Possible solutions
    - Brute force
    - HashMap
3. Coding
4. Tests
"""


# T=O(n^2), S=O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return [-1, -1]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# T=O(n), S=O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return [-1, -1]
        hash_map = {}
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [hash_map[target - x], i]
            hash_map[x] = i
