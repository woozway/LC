"""
1. Clarification
2. Possible solutions
 - flood fill, dfs or bfs
 - union find
3. Coding
4. Tests
"""


# # T=O(mn), S=O(mn), flood fill
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]: return 0
#         self.max_x = len(grid);
#         self.max_y = len(grid[0]);
#         self.grid = grid
#         self.visited = set()
#         return sum([self.floodfill_dfs(i, j) for i in range(self.max_x) for j in range(self.max_y)])
#
#     def floodfill_dfs(self, x, y):
#         if not self._is_valid(x, y):
#             return 0
#         self.visited.add((x, y))
#         for k in range(4):
#             self.floodfill_dfs(x + dx[k], y + dy[k])
#         return 1
#
#     def _is_valid(self, x, y):
#         if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
#             return False
#         if self.grid[x][y] == '0' or ((x, y) in self.visited):
#             return False
#         return True


# T=O(mn), S=O(mn), union find
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for d in directions:
                    nr, nc = i + d[0], j + d[1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        uf.union(i * n + j, nr * n + nc)
        return uf.count
