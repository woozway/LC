"""
1. Clarification
2. Possible solutions
     - dynamic programming v1
     - dp v2
3. Coding
4. Tests
"""


# T=O(rowIndex^2), S=O(1)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0: return []
        triangle = []
        for row_num in range(rowIndex + 1):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle[rowIndex]
       

# # T=O(rowIndex), S=O(1)
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         if rowIndex < 0: return []
#         row = [1] + [0] * rowIndex
#         for i in range(1, rowIndex + 1):
#             row[i] = row[i - 1] * (rowIndex - i + 1) // i
#         return row
