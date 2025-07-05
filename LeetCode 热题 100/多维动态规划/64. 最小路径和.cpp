// 状态表示：f[i,j]为到达(i,j)位置所有路径的数字总和；属性：Min
// 状态计算：按照上一步的坐标来划分集合：f[i,j] = min(f[i-1,j], f[i,j-1]) + a[i,j]
const int N = 210;
int f[N][N];
int a[N][N];

class Solution {
public:
  int minPathSum(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    for (int i = 1; i <= m; i ++ )
      for (int j = 1; j <= n; j ++ )
        a[i][j] = grid[i - 1][j - 1];

    memset(f, 0x3f, sizeof f);
    f[0][1] = f[1][0] = 0;
    
    for (int i = 1; i <= m; i ++ )
      for (int j = 1; j <= n; j ++ )
        f[i][j] = min(f[i - 1][j], f[i][j - 1]) + a[i][j];

    return f[m][n];
  }
};