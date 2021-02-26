"""
1. Clarification
2. Possible solutions
     - list operation
     - hash table
     - maths
     - Bit Manipulation
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(n)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         no_duplicate_list = []
#         for i in nums:
#             if i not in no_duplicate_list:
#                 no_duplicate_list.append(i)
#             else:
#                 no_duplicate_list.remove(i)
#         return no_duplicate_list.pop()


# T=O(n), S=O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = collections.defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i


# # T=O(n), S=O(n)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return 2 * sum(set(nums)) - sum(nums)


# # T=O(n), S=O(1)
# # a ^ 0 = a, a ^ a = 0, 
# # a ^ b ^ a = b ^ a ^ a = b ^ (a ^ a) = b ^ 0 = b
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         a = 0
#         for i in nums:
#             a ^= i
#         return a
