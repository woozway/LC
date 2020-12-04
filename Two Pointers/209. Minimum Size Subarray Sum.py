class Solution:
  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    """
    sliding window nums[i..j], O(n) solution
    """
    n = len(nums)
    i = 0
    j = -1
    total = 0
    ans = n+1
    while i < n:
      if j+1 < n and total < s:
        j += 1
        total += nums[j]
      else:
        total -= nums[i]
        i += 1
      if total >= s:
        ans = min(ans, j-i+1)
    return 0 if ans == n+1 else ans
