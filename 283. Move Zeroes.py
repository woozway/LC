class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        in-place implementation
        """
        n = len(nums)
        i = -1
        j = 0
        while j < n:
            if nums[j] != 0:
                i += 1
                nums[i] = nums[j]
            j += 1
        for k in range(i+1, n):
            nums[k] = 0
