class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    complement = [0] * 60
    ans = 0
    for x in time:
      x %= 60
      ans += complement[-x]
      complement[x] += 1
    return ans
