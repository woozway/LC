"""
1. Clarification
2. Possible solutions
    - Simulation + Set
    - Layer by layer
3. Coding
4. Tests
"""


# T=O(R*C), S=O(R*C)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        seen = set()
        ret = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(m * n):
            ret.append(matrix[r][c])
            seen.add((r, c))
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < m and 0 <= cc < n and (cr, cc) not in seen:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ret


# # T=O(R*C), S=O(1)
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
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

#         if not matrix or not matrix[0]: return []
#         ans = []
#         r1, r2 = 0, len(matrix) - 1
#         c1, c2 = 0, len(matrix[0]) - 1
#         while r1 <= r2 and c1 <= c2:
#             for r, c in spiral_coords(r1, c1, r2, c2):
#                 ans.append(matrix[r][c])
#             r1 += 1; r2 -= 1
#             c1 += 1; c2 -= 1
#         return ans
