class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        d = collections.Counter(nums)
        for num in nums:
            if num + 1 in d:
                res = max(res, d[num] + d[num + 1])
        return res
