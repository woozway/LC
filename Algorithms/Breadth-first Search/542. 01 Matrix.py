"""
1. Clarification
2. Possible solutions
     - bfs
     - dp v1
     - dp v2
3. Coding
4. Tests
"""


# T=O(nm), S=O(nm)
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        if n == 0 or m == 0: return [[]]
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        return dist


# # T=O(nm), S=O(1)
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         m, n = len(matrix), len(matrix[0])
#         if n == 0 or m == 0: return [[]]
#         dist = [[10**9] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     dist[i][j] = 0
#         for i in range(m):
#             for j in range(n):
#                 if i - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
#                 if j - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
#         for i in range(m - 1, -1, -1):
#             for j in range(n):
#                 if i + 1 < m:
#                     dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
#                 if j - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
#         for i in range(m):
#             for j in range(n - 1, -1, -1):
#                 if i - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
#                 if j + 1 < n:
#                     dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 if i + 1 < m:
#                     dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
#                 if j + 1 < n:
#                     dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
#         return dist


# # T=O(nm), S=O(1)
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         m, n = len(matrix), len(matrix[0])
#         if n == 0 or m == 0: return [[]]
#         dist = [[10**9] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     dist[i][j] = 0
#         for i in range(m):
#             for j in range(n):
#                 if i - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
#                 if j - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 if i + 1 < m:
#                     dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
#                 if j + 1 < n:
#                     dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
#         return dist
