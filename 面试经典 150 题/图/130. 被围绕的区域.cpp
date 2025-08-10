class Solution {
public:
  int m, n;
  vector<vector<char>> g;
  int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

  void dfs(int x, int y) {
    g[x][y] = 'A';
    for (int i = 0; i < 4; i ++ ) {
      int a = x + dx[i], b = y + dy[i];
      if (a >= 0 && a < m && b >=0 && b < n && g[a][b] == 'O')
        dfs(a, b);
    }
  }

  void solve(vector<vector<char>>& board) {
    if (!board.size()) return;
    g = board, m = board.size(), n = board[0].size();

    for (int i = 0; i < m; i ++ ) {
      if (g[i][0] == 'O') dfs(i, 0);
      if (g[i][n - 1] == 'O') dfs(i, n - 1);
    }

    for (int i = 1; i < n - 1; i ++ ) {
      if (g[0][i] == 'O') dfs(0, i);
      if (g[m - 1][i] == 'O') dfs(m - 1, i);
    }

    for (int i = 0; i < m; i ++ )
      for (int j = 0; j < n; j ++ )
        if (g[i][j] == 'A') g[i][j] = 'O';
        else g[i][j] = 'X';
    
    board = g;
  }
};