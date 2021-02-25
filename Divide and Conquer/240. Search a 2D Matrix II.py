"""
1. Clarification
2. Possible solutions
     - brute force
     - binary search
     - recursion or D&C
     - maths
3. Coding
4. Tests
"""


# # T=O(mn), S=O(1)
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]: return False
#         for row in matrix:
#             if target in row:
#                 return True
#         return False


# # T=O(lg(n!)), S=O(1)
# class Solution:
#     def binary_search(self, matrix, target, start, vertical):
#         lo = start
#         hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1
#         while hi >= lo:
#             mid = (lo + hi) // 2
#             if vertical:
#                 if matrix[start][mid] < target:
#                     lo = mid + 1
#                 elif matrix[start][mid] > target:
#                     hi = mid - 1
#                 else:
#                     return True
#             else:
#                 if matrix[mid][start] < target:
#                     lo = mid + 1
#                 elif matrix[mid][start] > target:
#                     hi = mid - 1
#                 else:
#                     return True
#         return False
#
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]: return False
#         for i in range(min(len(matrix), len(matrix[0]))):
#             vertical_found = self.binary_search(matrix, target, i, True)
#             horizontal_found = self.binary_search(matrix, target, i, False)
#             if vertical_found or horizontal_found:
#                 return True
#         return False


# T=O(nlgn), S=O(lgn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_rec(left, up, right, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            mid = left + (right - left) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

        if not matrix or not matrix[0]: return False
        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


# # T=O(n+m), S=O(1)
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]: return False
#         height = len(matrix)
#         width = len(matrix[0])
#         row = height - 1
#         col = 0
#         while col < width and row >= 0:
#             if matrix[row][col] > target:
#                 row -= 1
#             elif matrix[row][col] < target:
#                 col += 1
#             else:
#                 return True
#         return False
