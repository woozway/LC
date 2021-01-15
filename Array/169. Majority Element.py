"""
1. Clarification
2. Possible solutions
 - brute force
 - hashMap
 - sort
 - divide and conquer
 - Boyer-Moore algo
3. Coding
4. Tests
"""

# # T=O(n^2), S=O(1), Time Limit Exceeded
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         for i in range(n):
#             cnt = 0
#             for j in range(n):
#                 if nums[j] == nums[i]:
#                     cnt += 1
#                     if cnt > n // 2:
#                         return nums[i]

# # T=O(n), S=O(n)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         hashMap = collections.Counter(nums)
#         for k, v in hashMap.items():
#             if v > n // 2:
#                 return k

# # T=O(nlgn), S=O(1)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         n, pre, cnt = len(nums), nums[0], 1
#         nums.append('#')
#         for x in nums[1:]:
#             if x == pre:
#                 cnt += 1
#             else:
#                 if cnt > n // 2:
#                     return pre
#                 cnt = 1
#             pre = x

# T=O(nlgn), S=O(lgn)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.devi_n_conq(nums, 0, len(nums)-1)

    def devi_n_conq(self, nums, lo, hi):
        if lo == hi: return nums[lo]
        
        mid = lo + (hi - lo)//2
        left = self.devi_n_conq(nums, lo, mid)
        right = self.devi_n_conq(nums, mid+1, hi)
        if left == right: return left
        
        left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)
        return left if left_count > right_count else right

# # T=O(n), S=O(1), Boyer-Moore algo
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count, candidate = 0, None
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)
#         return candidate
