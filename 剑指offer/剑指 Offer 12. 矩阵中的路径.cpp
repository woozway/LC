// backtracking
// T=O(mn*3^l)
// S=O(min(l, mn))

class Solution {
  int n, m, l;
  string w;
public:
  bool exist(vector<vector<char>>& board, string word) {
    if (board.size() == 0 || board[0].size() == 0 || word.length() == 0) {
      return false;
    }
    n = board.size(), m = board[0].size(), l = word.length();
    w = word;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (backtrack(board, i, j, 0)) {
          return true;
        }
      }
    }
    return false;
  }

  bool backtrack(vector<vector<char>>& board, int r, int c, int index) {
    if (index == l) {
      return true;
    }
    if (!(r >= 0 && r < n) || !(c >= 0 && c < m)) {
      return false;
    }
    if (board[r][c] == w[index]) {
      char tmp = board[r][c];
      board[r][c] = '*';
      int dr[] = {-1,+1,0,0};
      int dc[] = {0,0,-1,+1};
      for (int i = 0; i < 4; i++) {
        int nr = r + dr[i], nc = c + dc[i];
        if (backtrack(board, nr, nc, index+1)) {
          return true;
        }
      }
      board[r][c] = tmp;
    }
    return false;
  }
};