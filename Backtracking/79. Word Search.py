"""
1. Clarification
2. Possible solutions
     - dfs + backtracking
     - trie + dfs + backtracking
3. Coding
4. Tests
"""


# dfs + backtracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or len(word) == 0: return False
        self.m, self.n, self.visited = len(board), len(board[0]), set()
        for i in range(self.m):
            for j in range(self.n):
                if self.check(board, word, i, j, 0):
                    return True
        return False

    def check(self, board, word, row, col, k):
        if board[row][col] != word[k]: return False
        if k == len(word) - 1: return True
        self.visited.add((row, col))
        result = False
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            newi, newj = row + di, col + dj
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                if (newi, newj) not in self.visited:
                    if self.check(board, word, newi, newj, k + 1):
                        result = True
                        break
        self.visited.remove((row, col))
        return result

    
# # trie + dfs + backtracking
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# END_OF_WORD = '#'
#
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board or not board[0]: return False
#         self.m, self.n, self.done = len(board), len(board[0]), False
#         root = dict()
#         node = root
#         for char in word:
#             node = node.setdefault(char, {})
#         node[END_OF_WORD] = END_OF_WORD
#         for i in range(self.m):
#             for j in range(self.n):
#                 if board[i][j] in root:
#                     self.dfs(board, i, j, '', root)
#                     if self.done:
#                         return True
#         return False
#
#     def dfs(self, board, row, col, cur_word, cur_dict):
#         cur_word += board[row][col]
#         cur_dict = cur_dict[board[row][col]]
#         if END_OF_WORD in cur_dict:
#             self.done = True
#             return
#         tmp, board[row][col] = board[row][col], '@'
#         for i in range(4):
#             x, y = row + dx[i], col + dy[i]
#             if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != '@' and board[x][y] in cur_dict:
#                 self.dfs(board, x, y, cur_word, cur_dict)
#                 if self.done:
#                     return
#         board[row][col] = tmp
