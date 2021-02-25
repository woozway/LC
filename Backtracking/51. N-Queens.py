"""
1. Clarification
2. Possible solutions
     - brute force
     - backtracking
3. Coding
4. Tests
"""


# T=O(n!), S=O(n)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1: return []
        self.result = []
        self.cols = set(); self.pie = set(); self.na = set()
        self.dfs(n, 0, [])
        return self._generate_result(n)

    def dfs(self, n, row, cur_list):
        if row >= n:
            self.result.append(cur_list)
            return
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            self.dfs(n, row + 1, cur_list + [col])
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append('.' * i + 'Q' + '.' * (n - i - 1))
        return [board[i:i+n] for i in range(0, len(board), n)]
