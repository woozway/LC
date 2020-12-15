class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    d = {}
    for x in arr:
      d[x] = d.get(x, 0) + 1
    s = set()
    for x in d.values():
      s.add(x)
    return True if len(s) == len(d) else False
