"""
1. Clarification
2. Possible solutions
    - Binary search II
3. Coding
4. Tests
"""


# T=O(lgn), S=O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return int(-inf)
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi -= 1
        return nums[lo]
