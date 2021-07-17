"""
1. Clarification
2. Possible solutions
    - Brute force
    - HashMap, c=-(a+b)
    - Two pointers (sort and find)
3. Coding
4. Tests
"""


# # T=O(n^3), S=O(1), Time Limit Exceeded
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) < 3: return []
#         nums.sort()
#         res = set()
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         res.add(tuple([nums[i], nums[j], nums[k]]))
#         return list(res)


# T=O(n^2), S=O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(map(list, res))


# T=O(n^2), S=O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0: r -= 1
                elif s < 0: l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1; r -= 1
        return res
