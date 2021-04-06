"""
1. Clarification
2. Possible solutions
    - Brute force
    - Binary search I
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


# T=O(lgn), S=O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
