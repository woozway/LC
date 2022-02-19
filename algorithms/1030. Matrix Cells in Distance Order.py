class Solution:
  def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    maxDist = max(r0, R-1-r0) + max(c0, C-1-c0)
    bucket = collections.defaultdict(list)
    dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)
    for i in range(R):
      for j in range(C):
        bucket[dist(i, j, r0, c0)].append([i, j])
    ret = []
    for i in range(maxDist + 1):
      ret.extend(bucket[i])
    return ret
