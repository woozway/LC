"""
1. Clarification
2. Possible solutions
 - brute force
 - sort and find
3. Coding
4. Tests
"""

# T=O(n^4), S=O(1), Time Limit Exceeded
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4: return []
        nums.sort()
        res = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            res.add((nums[i], nums[j], nums[k], nums[l]))
        return res

# T=O(n^3), S=O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums.sort()
        quadruplets = []
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target: break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target: continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target: break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target: continue
                l, r = j + 1, n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s > target: r -= 1
                    elif s < target: l += 1
                    else:
                        quadruplets.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]: l += 1
                        while l < r and nums[r] == nums[r - 1]: r -= 1
                        l += 1; r -= 1
        return quadruplets
