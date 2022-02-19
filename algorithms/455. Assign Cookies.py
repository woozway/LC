class Solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    j = cnt = 0
    for x in s:
      if j >= len(g):
        break
      else:
        if x >= g[j]:
          cnt += 1
          j += 1
    return cnt
