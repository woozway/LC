class Solution:
  def maxPower(self, s: str) -> int:
    return max(len(list(x)) for _, x in groupby(s))
