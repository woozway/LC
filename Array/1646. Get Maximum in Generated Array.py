class Solution:
  def getMaximumGenerated(self, n: int) -> int:
    nums = [0,1] + [0]*(n-1)
    if n < 2: return nums[n]
    for i in range(2, n+1):
      if i % 2 == 0 and i//2 <= n:
        nums[i] = nums[i//2]
      if i % 2 == 1 and i//2 + 1 <= n:
        nums[i] = nums[i//2] + nums[i//2+1]
    return max(nums)
