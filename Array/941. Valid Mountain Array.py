"""
1. Clarification
2. Possible solutions
 - one pass
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if not arr: return False
        n = len(arr)
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1
