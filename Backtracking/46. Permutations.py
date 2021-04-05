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
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        if not nums: return []
        n = len(nums)
        res = []
        backtrack()
        return res


# T=O(n*n!), S=O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        return list(itertools.permutations(nums))
