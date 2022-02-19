"""
1. Clarification
2. Possible solutions
    - Sorting
    - HashSet
    - Bit Manipulation
    - Gauss' Formula
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num


# T=O(n), S=O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


# T=O(n), S=O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


# T=O(n), S=O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums)+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
