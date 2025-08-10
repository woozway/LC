const int N = 10;

class Solution {
  string w;
  vector<vector<char>> g;
  bool st[N][N];
  int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

  bool dfs(int u, int x, int y) {
    if (u == w.size()) return true;

    st[x][y] = true;
    for (int i = 0; i < 4; i ++ ) {
      int a = x + dx[i], b = y + dy[i];
      if (a >= 0 && a < g.size() && b >= 0 && b < g[0].size() && !st[a][b] && g[a][b] == w[u])
        if (dfs(u + 1, a, b)) return true;
    }
    st[x][y] = false;
    
    return false;
  }

public:
  bool exist(vector<vector<char>>& board, string word) {
    memset(st, 0, sizeof st), w = word, g = board;
    int m = board.size(), n = board[0].size();

    for (int i = 0; i < m; i ++ )
      for (int j = 0; j < n; j ++ )
        if (g[i][j] == word[0])
          if (dfs(1, i, j)) return true;

    return false;
  }
};