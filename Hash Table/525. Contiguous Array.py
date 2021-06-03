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
        maxLength, counter, n = 0, 0, len(nums)
        for i in range(n):
            if nums[i] == 1:
                counter += 1
            else:
                counter -= 1
            if counter in mp:
                prevIndex = mp[counter]
                maxLength = max(maxLength, i - prevIndex)
            else:
                mp[counter] = i
        return maxLength
