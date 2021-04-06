"""
1. Clarification
2. Possible solutions
    - Sort
    - Set
    - Floyd's Tortoise and Hare (Cycle Detection)
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


# T=O(n), S=O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


# T=O(n), S=O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare
