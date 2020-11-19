class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= (m*n)
        a = [grid[i][j] for i in range(m) for j in range(n)]
        b = list(reversed(a[:m*n-k])) + list(reversed(a[m*n-k:]))
        b.reverse()
        return [b[i*n:n+i*n] for i in range(m)]
