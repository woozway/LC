"""
1. Clarification
2. Possible solutions
    - Brute force
    - Binary Search I
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = -1
        for i in range(1, n - 1):
            if arr[i] > arr[i + 1]:
                ans = i
                break
        return ans


# T=O(lgn), S=O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
