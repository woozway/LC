"""
1. Clarification
2. Possible solutions
    - Backtracking
    - Python library function
3. Coding
4. Tests
"""


# T=O(n*n!), S=O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        self.ans = []
        self.backtrack(nums, 0)
        return self.ans

    def backtrack(self, nums, idx):
        if idx == len(nums):
            self.ans.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.backtrack(nums, idx + 1)
            nums[i], nums[idx] = nums[idx], nums[i]


# T=O(n*n!), S=O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        return list(itertools.permutations(nums))
