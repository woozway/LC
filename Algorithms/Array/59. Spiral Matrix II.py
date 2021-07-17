"""
1. Clarification
2. Possible solutions
     - Simulation + Set
     - Layer by layer
3. Coding
4. Tests
"""


# T=O(n*n), S=O(n*n)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1: return [[]]
        ret = [[0] * n for _ in range(n)]
        visited = set()
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        num = 1
        for _ in range(n * n):
            ret[r][c] = num
            num += 1
            visited.add((r, c))
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                r, c = nr, nc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ret


# # T=O(n*n), S=O(1)
# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         def spiral_coords(r1, c1, r2, c2):
#             for c in range(c1, c2 + 1):
#                 yield r1, c
#             for r in range(r1 + 1, r2 + 1):
#                 yield r, c2
#             if r1 < r2 and c1 < c2:
#                 for c in range(c2 - 1, c1, -1):
#                     yield r2, c
#                 for r in range(r2, r1, -1):
#                     yield r, c1

#         if n < 1: return [[]]
#         ret = [[0] * n for _ in range(n)]
#         r1, r2 = 0, n - 1
#         c1, c2 = 0, n - 1
#         num = 1
#         while r1 <= r2 and c1 <= c2:
#             for r, c in spiral_coords(r1, c1, r2, c2):
#                 ret[r][c] = num
#                 num += 1
#             r1 += 1; r2 -= 1
#             c1 += 1; c2 -= 1
#         return ret
