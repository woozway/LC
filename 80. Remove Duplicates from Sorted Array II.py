class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre = -100000
        cnt = 0
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] != pre:
                i += 1
                nums[i] = nums[j]
                cnt = 1
            elif cnt < 2:
                i += 1
                nums[i] = nums[j]
                cnt += 1
            pre = nums[j]
            j += 1
        return i+1
