class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            if target-nums[i] in d:
                return [d[target-x], i]
            d[x] = i
        return []
