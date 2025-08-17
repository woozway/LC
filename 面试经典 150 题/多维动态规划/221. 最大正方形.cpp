// 状态表示：f[i,j]表示以(i,j)为右下角坐标的正方形边长；属性：Max
// 状态计算：按照f[i,j] = min(f[i-1,j-1], f[i-1,j], f[i,j-1]) + 1 if a[i,j] = 1 else 0
const int N = 310;
int a[N][N];
int f[N][N];

class Solution {
public:
  int maximalSquare(vector<vector<char>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();

    for (int i = 1; i <= m; i ++ )
      for (int j = 1; j <= n; j ++ )
        a[i][j] = matrix[i - 1][j - 1];
    
    memset(f, 0, sizeof f);
    int res = 0;
    for (int i = 1; i <= m; i ++ )
      for (int j = 1; j <= n; j ++ )
        if (a[i][j] == '1') {
          f[i][j] = min({f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]}) + 1;
          res = max(res, f[i][j]);
        }

    return res * res;
  }
};