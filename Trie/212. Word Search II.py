"""
1. Clarification
2. Possible solutions
 - naive dfs
 - trie + dfs + backtracking
3. Coding
4. Tests
"""

# trie + dfs + backtracking
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

END_OF_WORD = '#'

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words: return []
        self.result = set()
        root = dict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[END_OF_WORD] = END_OF_WORD
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    self.dfs(board, i, j, '', root)
        return list(self.result)

    def dfs(self, board, row, col, cur_word, cur_dict):
        cur_word += board[row][col]
        cur_dict = cur_dict[board[row][col]]
        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)
        tmp, board[row][col] = board[row][col], '@'
        m, n = len(board), len(board[0])
        for i in range(4):
            x, y = row + dx[i], col + dy[i]
            if 0 <= x < m and 0 <= y < n and board[x][y] != '@' and board[x][y] in cur_dict:
                self.dfs(board, x, y, cur_word, cur_dict)
        board[row][col] = tmp
