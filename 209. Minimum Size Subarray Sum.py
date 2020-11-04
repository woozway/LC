class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        O(n) solution
        """
        n = len(nums)
        if n < 1 or sum(nums) < s:
            return 0
        i = 0
        j = -1
        total = 0
        res = n+1
        while i <= n-1:
            if j+1 < n and total < s:
                j += 1
                total += nums[j]
            else:
                total -= nums[i]
                i += 1
            if total >= s:
                res = min(res, j-i+1)
        if res == n+1:
            return 0
        return res
