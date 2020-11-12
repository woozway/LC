class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        ans = [[0]*m for i in range(n)]
        for r, c in indices:
            for i in range(m):
                ans[r][i] += 1
            for i in range(n):
                ans[i][c] += 1
        return sum(1 for i in range(n) for j in range(m) if ans[i][j]%2 == 1)
