"""
1. Clarification
2. Possible solutions
    - Prefix-Sum + Hash
3. Coding
4. Tests
"""


# T=O(n), S=O(n)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0: -1}
        count, maxLen, n = 0, 0, len(nums)
        for i in range(n):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in mp:
                prevIndex = mp[count]
                maxLen = max(maxLen, i - prevIndex)
            else:
                mp[count] = i
        return maxLen
