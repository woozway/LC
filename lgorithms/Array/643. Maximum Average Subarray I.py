class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    n = len(nums)
    newsum = maxsum = sum(nums[0:k])
    for i in range(k, n):
      newsum += nums[i] - nums[i-k]
      maxsum = max(maxsum, newsum)
    return maxsum / k
