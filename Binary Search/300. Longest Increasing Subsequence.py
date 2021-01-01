class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for i in range(len(nums)):
            p = bisect.bisect_left(lis, nums[i])
            if p == len(lis):
                lis.append(nums[i])
            else:
                lis[p] = nums[i]
        return len(lis)
