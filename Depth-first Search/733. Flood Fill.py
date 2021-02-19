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


# # T=O(RC), S=O(RC)
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         currColor = image[sr][sc]
#         if currColor == newColor: return image
#         n, m = len(image), len(image[0])
#         que = collections.deque([(sr, sc)])
#         image[sr][sc] = newColor
#         while que:
#             x, y = que.popleft()
#             for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
#                 if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
#                     que.append((mx, my))
#                     image[mx][my] = newColor
#         return image
