"""
1. Clarification
2. Possible solutions
     - HashMap
3. Coding
4. Tests
"""


# T=O(n), S=O(min(n, k))
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False
