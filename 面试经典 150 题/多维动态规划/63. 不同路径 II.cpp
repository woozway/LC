// 状态表示：f[i,j]表示到达(i,j)的可行方案数；属性：数量
// 状态计算：按照到达(i,j)的上一步来划分集合：f[i,j] = f[i-1,j] + f[i,j-1]
const int N = 110;
int a[N][N];
int f[N][N];

class Solution {
public:
  int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
    int m = obstacleGrid.size(), n = obstacleGrid[0].size();
    auto &a = obstacleGrid;

    memset(f, 0, sizeof f);
    for (int i = 0; i < m; i ++ )
      if (a[i][0] == 1) f[i][0] = 0;
      else if (i && !f[i - 1][0]) f[i][0] = 0;
      else f[i][0] = 1;
    for (int i = 0; i < n; i ++ )
      if (a[0][i] == 1) f[0][i] = 0;
      else if (i && !f[0][i - 1]) f[0][i] = 0;
      else f[0][i] = 1;

    for (int i = 1; i < m; i ++ )
      for (int j = 1; j < n; j ++ )
        if (a[i][j] == 1) f[i][j] = 0;
        else f[i][j] = f[i - 1][j] + f[i][j - 1];

    return f[m - 1][n - 1];
  }
};