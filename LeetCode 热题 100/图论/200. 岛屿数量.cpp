class Solution {
  int m, n;
  vector<vector<char>> g;
  int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

  void dfs(int x, int y) {
    if (x < 0 || x >= m || y < 0 || y >= n) return;
    if (g[x][y] != '1') return;

    g[x][y] = '2';

    for (int i = 0; i < 4; i ++ ) dfs(x + dx[i], y + dy[i]);
  }

public:
  int numIslands(vector<vector<char>>& grid) {
    g = grid;
    m = g.size(), n = g[0].size();

    // 找到未打上标记的陆地（1），进入dfs，统计总陆地数量
    int res = 0;
    for (int i = 0; i < m; i ++ )
      for (int j = 0; j < n; j ++ )
        if (g[i][j] == '1') {
          dfs(i, j);
          res ++ ;
        }
    return res;
  }
};