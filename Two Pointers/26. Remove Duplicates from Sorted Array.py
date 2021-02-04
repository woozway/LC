class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    pre = -100000
    i = -1
    j = 0
    while j < len(nums):
      if nums[j] != pre:
        i += 1
        nums[i] = nums[j]
      pre = nums[j]
      j += 1
    return i+1
