const int N = 20;
typedef pair<int, int> PII;

class Solution {
  int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
  int d[N][N];
  
public:
  int orangesRotting(vector<vector<int>>& grid) {
    memset(d, 0, sizeof d);
    auto &g = grid;
    int m = g.size(), n = g[0].size();

    // 将所有腐烂的橘子（2）入队，层序遍历朝4个方向往外感染新鲜橘子（1）
    queue<PII> q;
    for (int i = 0; i < m; i ++ )
      for (int j = 0; j < n; j ++ )
        if (g[i][j] == 2) q.push({i, j});
    
    while (q.size()) {
      int sz = q.size();
      for (int i = 0; i < sz; i ++ ) {
        auto [x, y] = q.front(); q.pop();
        for (int j = 0; j < 4; j ++ ) {
          int a = x + dx[j], b = y + dy[j];
          if (a >= 0 && a < m && b >= 0 && b < n && g[a][b] == 1) {
            g[a][b] = 2;
            d[a][b] = d[x][y] + 1;
            q.push({a, b});
          }
        }
      }
    }

    // 若还存在新鲜橘子（1），返回-1，否则返回耗时
    int res = 0;
    for (int i = 0; i < m; i ++ )
      for (int j = 0; j < n; j ++ )
        if (g[i][j] == 1) return -1;
        else res = max(res, d[i][j]);

    return res;
  }
};