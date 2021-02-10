"""
1. Clarification
2. Possible solutions
 - binary search
3. Coding
4. Tests
"""


# T=O(lgn), S=O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return int(-inf)
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]
