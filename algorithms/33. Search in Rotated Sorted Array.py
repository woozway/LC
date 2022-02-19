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


# T=O(lgn), S=O(1), see also leetcode 81.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
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
        return -1


# T=O(lgn), S=O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
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
        return -1

