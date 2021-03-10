"""
1. Clarification
2. Possible solutions
     - Brute force
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
#         for k in range(m + n - 1):
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
        for d in range(m + n - 1):
            intermediate.clear()
            r, c = 0 if d < n else d - n + 1, d if d < n else n - 1
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
#         row, column = 0, 0
#         direction = 1
#         result = []
#         while row < m and column < n:
#             result.append(matrix[row][column])
#             new_row = row + (-1 if direction == 1 else 1)
#             new_column = column + (1 if direction == 1 else -1)
#             if new_row < 0 or new_row == m or new_column < 0 or new_column == n:
#                 if direction:
#                     row += (column == n - 1)
#                     column += (column < n - 1)
#                 else:
#                     column += (row == m - 1)
#                     row += (row < m - 1)
#                 direction = 1 - direction
#             else:
#                 row = new_row
#                 column = new_column
#         return result
