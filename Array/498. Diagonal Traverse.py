"""
1. Clarification
2. Possible solutions
     - Brute force, index sum: r + c = d
     - Diagonal iteration and reversal
     - Simulation
3. Coding
4. Tests
"""


# # T=O(m*n*(m+n)), S=O(max(m,n)), Time Limit Exceeded
# class Solution:
#     def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]: return []
#         m, n = len(matrix), len(matrix[0])
#         ans = []
#         for k in range(m-1 + n-1 + 1):
#             tmp = []
#             for i in range(m):
#                 for j in range(n):
#                     if i + j == k:
#                         tmp.append(matrix[i][j])
#             if k % 2 == 0:
#                 tmp.reverse()
#             ans += tmp
#         return ans


# T=O(m*n), S=O(min(m,n))
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        result, intermediate = [], []
        for d in range(m-1 + n-1 + 1):
            intermediate.clear()
            r, c = 0 if d < n else d - (n-1), d - 0 if d < n else n - 1
            while r < m and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result


# # T=O(m*n), S=O(1)
# class Solution:
#     def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]: return []
#         m, n = len(matrix), len(matrix[0])
#         ret = []
#         r, c = 0, 0
#         direction = 1
#         while r < m and c < n:
#             ret.append(matrix[r][c])
#             new_r = r + (-1 if direction else +1)
#             new_c = c + (+1 if direction else -1)
#             if not (0 <= new_r < m) or not (0 <= new_c < n):
#                 if direction:
#                     r += (c == n - 1)
#                     c += (c < n - 1)
#                 else:
#                     c += (r == m - 1)
#                     r += (r < m - 1)
#                 direction = 1 - direction
#             else:
#                 r, c = new_r, new_c
#         return ret
