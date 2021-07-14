"""
1. Clarification
2. Possible solutions
    - Sorting
    - Median
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


# T=O(n), S=O(1)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        self.findMedian(nums, 0, len(nums) - 1)
        half = (len(nums) + 1) // 2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

    def findMedian(self, nums, left, right):
        i = j = k = left + 1
        mid = len(nums) // 2
        sentinel = nums[left]
        while k <= right:
            if nums[k] < sentinel:
                nums[k], nums[j] = nums[j], nums[k]
                nums[i], nums[j] = nums[j], nums[i]
                i, j, k = i + 1, j + 1, k + 1
            elif nums[k] > sentinel:
                k += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                j, k = j + 1, k + 1
        nums[left], nums[i-1] = nums[i-1], nums[left]
        if i - 1 <= mid < j:
            return nums[mid]
        if mid >= j:
            return self.findMedian(nums, j, right)
        else:
            return self.findMedian(nums, left, i - 2)
