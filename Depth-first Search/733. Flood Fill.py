"""
1. Clarification
2. Possible solutions
     - dfs
     - bfs
3. Coding
4. Tests
"""


# T=O(RC), S=O(RC)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r - 1, c)
                if r + 1 < R: dfs(r + 1, c)
                if c >= 1: dfs(r, c - 1)
                if c + 1 < C: dfs(r, c + 1)
        dfs(sr, sc)
        return image


# # T=O(mn), S=O(mn)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.m, self.n, self.image = len(image), len(image[0]), image
        if not (0 <= sr < self.m) or not (0 <= sc < self.n): return [[]]
        if image[sr][sc] != newColor:
            self.bfs(sr, sc, newColor)
        return image

    def bfs(self, sr, sc, newColor):
        Q = collections.deque([(sr, sc)])
        visited = set([(sr, sc)])
        ori_color = self.image[sr][sc]
        self.image[sr][sc] = newColor
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        while Q:
            r, c = Q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < self.m and 0 <= nc < self.n \
                        and (nr, nc) not in visited and self.image[nr][nc] == ori_color:
                    Q.append((nr, nc))
                    visited.add((nr, nc))
                    self.image[nr][nc] = newColor
