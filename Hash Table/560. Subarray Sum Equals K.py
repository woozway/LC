"""
1. Clarification
2. Possible solutions
    - Brute force
    - Prefix sum + Hash
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1), Time Limit Exceeded
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         for start in range(len(nums)):
#             Sum = 0
#             for end in range(start, -1, -1):
#                 Sum += nums[end]
#                 if Sum == k:
#                     count += 1
#         return count


# T=O(n), S=O(n), see also leetcode 1074.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = collections.Counter()
        hashMap[0] = 1
        count, pre = 0, 0
        for num in nums:
            pre += num
            if hashMap[pre - k]:
                count += hashMap[pre - k]
            hashMap[pre] += 1
        return count
