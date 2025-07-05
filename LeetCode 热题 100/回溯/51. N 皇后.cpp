const int N = 20;
char g[N][N];
int col[N], dg[N], adg[N];

class Solution {
  int m;
  vector<vector<string>> res;

  void dfs(int u) {
    if (u == m) {
      vector<string> path;
      for (int i = 0; i < m; i ++ ) {
        string s = "";
        for (int j = 0; j < m; j ++ ) s += g[i][j];
        path.push_back(s);
      }
      res.push_back(path);
      return;
    }

    for (int i = 0; i < m; i ++ )
      if (!col[i] && !dg[u + i] && !adg[u - i + m]) {
        col[i] = dg[u + i] = adg[u - i + m] = true;
        g[u][i] = 'Q';
        dfs(u + 1);
        g[u][i] = '.';
        col[i] = dg[u + i] = adg[u - i + m] = false;
      }
  }

public:
  vector<vector<string>> solveNQueens(int n) {
    memset(col, 0, sizeof col), memset(dg, 0, sizeof dg), memset(adg, 0, sizeof adg);
    for (int i = 0; i < n; i ++ )
      for (int j = 0; j < n; j ++ )
        g[i][j] = '.';

    m = n;
    dfs(0);
    return res;
  }
};