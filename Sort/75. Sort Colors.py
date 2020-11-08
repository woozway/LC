class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        invariant: [0...lt] as 0's, [gt...len(nums)-1] as 2's
        without using the library's sort function
        with a one-pass algorithm using only O(1) constant space
        """
        lt = -1
        gt = len(nums)
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
