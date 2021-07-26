// depth-first search
// T=O(mn)
// T=O(mn)

class Solution {
  int count, m, n;
public:
  int movingCount(int m, int n, int k) {
    vector<vector<int>> board(m, vector<int>(n));
    vector<vector<int>> visited(m, vector<int>(n));
    this->m = m, this->n = n;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int sum = 0;
        string si = to_string(i);
        for (auto ch : si) {
          sum += ch - '0';
        }
        string sj = to_string(j);
        for (auto ch : sj) {
          sum += ch - '0';
        }
        if (sum <= k) {
          board[i][j] = 1;
        }
      }
    }
    dfs(board, 0, 0, visited);
    return count;
  }

  void dfs(vector<vector<int>> &board, int r, int c, vector<vector<int>> &visited) {
    if (!(r >= 0 && r < m) || !(c >= 0 && c < n) || board[r][c] == 0 || visited[r][c]) {
      return;
    }
    visited[r][c] = 1;
    count += 1;
    int dr[] = {-1,+1,0,0};
    int dc[] = {0,0,-1,+1};
    for (int i = 0; i < 4; i++) {
      int nr = r + dr[i], nc = c + dc[i];
      dfs(board, nr, nc, visited);
    }
  }
};