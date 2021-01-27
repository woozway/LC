"""
1. Clarification
2. Possible solutions
 - simple backtracking + naive dfs
3. Coding
4. Tests
"""

# T=O(1), S=O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    c = board[i][j]
                    board[i][j] = '.'
                    if not self.isValid(board, i, j, c):
                        return False
                    board[i][j] = c
        return True

    def isValid(self, board, row, col, c):
        for i in range(len(board)):
            if board[row][i] == c: return False
            if board[i][col] == c: return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == c: return False
        return True
