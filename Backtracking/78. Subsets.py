"""
1. Clarification
2. Possible solutions
    - Cascading
    - Backtracking v1
    - Backtracking v2
    - Lexicographic (Binary Sorted) Subsets
3. Coding
4. Tests
"""


# T=O(n*2^n), S=O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output


# T=O(n*2^n), S=O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        n = len(nums)
        ans, tmp = [], []

        def backtrack(idx):
            if idx == n:
                ans.append(tmp[:])
                return
            tmp.append(nums[idx])
            backtrack(idx + 1)
            tmp.pop()
            backtrack(idx + 1)

        backtrack(0)
        return ans


# T=O(n*2^n), S=O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


# T=O(n*2^n), S=O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        for i in range(2 ** n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return output
