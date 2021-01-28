"""
1. Clarification
2. Possible solutions
 - backtracking
 - bit manipulation
3. Coding
4. Tests
"""

# # T=O(n!), S=O(n)
# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         if n < 1: return 0
#         self.count = 0
#         self.cols = set(); self.pie = set(); self.na = set()
#         self.dfs(n, 0, [])
#         return self.count
# 
#     def dfs(self, n, row, cur_list):
#         if row >= n:
#             self.count += 1
#             return
#         for col in range(n):
#             if col in self.cols or row + col in self.pie or row - col in self.na:
#                 continue
#             self.cols.add(col)
#             self.pie.add(row + col)
#             self.na.add(row - col)
#             self.dfs(n, row + 1, cur_list + [col])
#             self.cols.remove(col)
#             self.pie.remove(row + col)
#             self.na.remove(row - col)

# T=O(n!), S=O(n)
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1: return 0
        self.count = 0
        self._dfs(n, 0, 0, 0, 0)
        return self.count

    def _dfs(self, n, row, cols, pie, na):
        if row >= n:
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits
            self._dfs(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            bits &= bits - 1
