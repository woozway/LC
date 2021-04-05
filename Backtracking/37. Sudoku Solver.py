"""
1. Clarification
2. Possible solutions
    - Simple backtracking + naive dfs
    - Backtracking + preprocessing + handle blanks with minimun optional number
    - Advanced data structure: DancingLinks
3. Coding
4. Tests
"""


# simple backtracking + naive dfs
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        if not board: return
        self.dfs(board)

    def dfs(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    continue
                for c in '123456789':
                    if self.isValid(board, i, j, c):
                        board[i][j] = c
                        if self.dfs(board):
                            return True
                        board[i][j] = '.'
                return False
        return True

    def isValid(self, board, row, col, c):
        for i in range(len(board)):
            if board[row][i] == c: return False
            if board[i][col] == c: return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == c: return False
        return True
