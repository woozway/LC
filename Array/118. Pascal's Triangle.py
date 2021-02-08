"""
1. Clarification
2. Possible solutions
 - dynamic programming v1
 - dynamic programming v2
3. Coding
4. Tests
"""


# T=O(n^2), S=O(1)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0: return []
        ans = [[0] * (i + 1) for i in range(numRows)]
        for i in range(0, numRows):
            for j in range(i + 1):
                ans[i][j] = 1 if j == 0 or j == i else ans[i - 1][j - 1] + ans[i - 1][j]
        return ans


# # T=O(n^2), S=O(1)
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         if numRows <= 0: return []
#         triangle = []
#         for row_num in range(numRows):
#             row = [None for _ in range(row_num + 1)]
#             row[0], row[-1] = 1, 1
#             for j in range(1, len(row) - 1):
#                 row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
#             triangle.append(row)
#         return triangle
