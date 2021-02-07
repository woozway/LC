"""
1. Clarification
2. Possible solutions
 - brute force
 - prefix sum + binary search
 - two pointers
3. Coding
4. Tests
"""


# # T=O(n^2), S=O(1), Time Limit Exceeded
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if target < 1 or not nums: return 0
#         n = len(nums)
#         ans = n + 1
#         for i in range(n):
#             total = 0
#             for j in range(i, n):
#                 total += nums[j]
#                 if total >= target:
#                     ans = min(ans, j - i + 1)
#                     break
#         return 0 if ans == n + 1 else ans


# # T=O(nlgn), S=O(n)
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if target < 1 or not nums: return 0
#         n = len(nums)
#         ans = n + 1
#         sums = [0]
#         for i in range(n):
#             sums.append(sums[-1] + nums[i])
#         for i in range(n):
#             tmp = target + sums[i]
#             bound = bisect.bisect_left(sums, tmp)
#             if bound != len(sums):
#                 ans = min(ans, bound - i)
#         return 0 if ans == n + 1 else ans


# T=O(n), S=O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target < 1 or not nums: return 0
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans
