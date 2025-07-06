"""
1. Clarification
2. Possible solutions
    - Brute force
    - Two pointers v1
    - Two pointers v2
3. Coding
4. Tests
"""


# T=O(n^2), S=O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        left, length_ = 0, len(nums) - 1
        while left <= length_:
            if left > length_:
                break
            if nums[left] == val:
                for j in range(left + 1, length_ + 1):
                    nums[j - 1] = nums[j]
                length_ -= 1
            else:
                left += 1
        return length_ + 1


# T=O(n), S=O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i, n = 0, len(nums)
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


# T=O(n), S=O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
