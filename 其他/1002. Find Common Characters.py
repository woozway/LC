class Solution:
  def commonChars(self, A: List[str]) -> List[str]:
    return list(reduce(lambda x, y: x & y, map(Counter, A)).elements())
