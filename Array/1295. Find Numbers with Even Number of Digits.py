"""
1. Clarification
2. Possible solutions
 - str
 - log
3. Coding
4. Tests
"""


# T=O(n), S=O(1)
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if not nums: return 0
        return sum(1 for num in nums if len(str(num)) % 2 == 0)


# # T=O(n), S=O(1)
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         if not nums: return 0
#         return sum(1 for num in nums if int(math.log10(num) + 1) & 1 == 0)
