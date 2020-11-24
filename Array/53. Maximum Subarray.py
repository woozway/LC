class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    maxn = -inf
    subsum = 0
    for x in nums:
      subsum += x
      maxn = max(maxn, subsum)
      if subsum < 0:
        subsum = 0
    return maxn
