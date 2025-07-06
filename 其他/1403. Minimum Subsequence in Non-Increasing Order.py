class Solution:
  def minSubsequence(self, nums: List[int]) -> List[int]:
    nums.sort(reverse=True)
    ret = list()
    runningSum, Sum = 0, sum(nums)
    for num in nums:
      runningSum += num
      ret.append(num)
      if runningSum > Sum - runningSum:
        return ret
