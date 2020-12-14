class Solution:
  def surfaceArea(self, grid: List[List[int]]) -> int:
    N = len(grid)
    ans = 0
    for r in range(N):
      for c in range(N):
        if grid[r][c]:
          ans += 2
          for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            nval = grid[nr][nc] if 0 <= nr < N and 0 <= nc < N else 0
            ans += max(grid[r][c] - nval, 0)
    return ans
