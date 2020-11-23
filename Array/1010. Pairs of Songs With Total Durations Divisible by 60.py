class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    a = [0] * 60
    ans = 0
    for t in time:
      t %= 60
      ans += a[-t]
      a[t] += 1
    return ans
