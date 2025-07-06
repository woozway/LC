class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    a = sorted(set(arr))
    d = {}
    for i, v in enumerate(a, 1):
      d[v] = i
    return [d[x] for x in arr]
