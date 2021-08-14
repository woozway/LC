"""
1. Clarification
2. Possible solutions
    - Binary search I
3. Coding
4. Tests
"""


# T=O(lgn)*, S=O(1), see also leetcode 33.
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        n = len(nums)
        if n == 1: return nums[0] == target
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] == nums[hi]:
                lo, hi = lo+1, hi-1
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
        return False


# T=O(lgn)*, S=O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        n = len(nums)
        if n == 1: return nums[0] == target
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] == nums[hi]:
                lo, hi = lo+1, hi-1
            elif nums[mid] <= nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
            else:
                if nums[lo] <= target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
        return False

