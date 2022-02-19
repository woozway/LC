"""
1. Clarification
2. Possible solutions
    - Simple backtracking
    - One iteration
3. Coding
4. Tests
"""


# T=O(1), S=O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]: return False
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    c = board[i][j]
                    board[i][j] = '.'
                    if not self.isValid(board, i, j, c):
                        return False
                    board[i][j] = c
        return True

    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[row][i] == c: return False
            if board[i][col] == c: return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == c: return False
        return True


# T=O(1), S=O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]: return False
        rows = [collections.Counter() for _ in range(9)]
        cols = [collections.Counter() for _ in range(9)]
        boxes = [collections.Counter() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    if rows[i][num] or cols[j][num] or boxes[box_index][num]:
                        return False
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
        return True
