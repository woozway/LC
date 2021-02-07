"""
1. Clarification
2. Possible solutions
 - sort
 - hashMap
3. Coding
4. Tests
"""


# T=O(nlgn), S=O(n)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not nums or len(nums) % 2: return 0
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans


# # T=O(n), S=O(n)
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         if not nums or len(nums) % 2: return 0
#         count = collections.Counter()
#         for num in nums:
#             count[num] += 1
#         d, Sum = 0, 0
#         for i in range(-10000, 10001):
#             Sum += (count[i] + 1 - d) // 2 * i
#             d = (2 + count[i] - d) % 2
#         return Sum
