"""
1. Clarification
2. Possible solutions
     - Sort
     - One Pass
3. Coding
4. Tests
"""


# # T=O(nlgn), S=O(n)
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         if not nums: return -float('inf')
#         n = len(nums)
#         distinct = {x for x in nums}
#         sz = len(distinct)
#         ordered = sorted(distinct)
#         return ordered[-1] if sz < 3 else ordered[-3]


# T=O(n), S=O(1)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums: return -float('inf')
        a = b = c = -float('inf')
        for n in nums:
            if n in (a, b, c): continue
            if n > a: n, a = a, n
            if n > b: n, b = b, n
            if n > c: n, c = c, n
        return a if c == -float('inf') else c
