class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        without using the library's sort function
        with a one-pass algorithm using only O(1) constant space
        """
        n = len(nums)

        lt = -1
        gt = n
        i = 0

        while i < gt:
            if nums[i] == 0:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            elif nums[i] == 2:
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
            else:
                i += 1
