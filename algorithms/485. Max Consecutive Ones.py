"""
1. Clarification
2. Possible solutions
    - One pass
    - Pythonic
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums: return 0
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)


# T=O(n), S=O(n)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums: return 0
        return max(map(len, ''.join(map(str, nums)).split('0')))
