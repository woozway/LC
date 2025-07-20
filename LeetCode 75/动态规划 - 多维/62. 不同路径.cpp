// 状态表示：f[i,j]为到达(i,j)的路径数；属性：数量
// 状态计算：按照上一步的坐标来划分集合：f[i,j] = f[i-1,j] + f[i,j-1]
const int N = 110;
int f[N][N];

class Solution {
public:
  int uniquePaths(int m, int n) {
    memset(f, 0, sizeof f);

    for (int i = 0; i < m; i ++ ) f[i][0] = 1;
    for (int i = 0; i < n; i ++ ) f[0][i] = 1;

    for (int i = 1; i < m; i ++ )
      for (int j = 1; j < n; j ++ )
        f[i][j] = f[i - 1][j] + f[i][j - 1];
    
    return f[m - 1][n - 1];
  }
};