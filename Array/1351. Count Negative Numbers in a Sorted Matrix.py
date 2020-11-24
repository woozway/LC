class Solution:
  def countNegatives(self, grid: List[List[int]]) -> int:
    """
    T=O(n)
    """
    n = len(grid[0])
    cnt = 0
    pos = n-1
    for l in grid:
      i = pos
      while i >= 0:
        if l[i] >= 0:
          if i+1 < n:
            cnt += n-i-1
            pos = i+1
          break
        i -= 1
      if i == -1:
        cnt += n
        pos = -1
    return cnt
