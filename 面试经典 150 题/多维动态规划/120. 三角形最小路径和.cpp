const int N = 210, INF = 1e9;
int n;
int a[N][N];
int f[N][N];

class Solution {
public:
  int minimumTotal(vector<vector<int>>& triangle) {
    n = triangle.size();
    for (int i = 1; i <= n; i ++ )
      for (int j = 1; j <= i; j ++ )
        a[i][j] = triangle[i - 1][j - 1];

    for (int i = 0; i <= n; i ++ )
      for (int j = 0; j <= i + 1; j ++ )
        f[i][j] = INF;
    
    f[1][1] = a[1][1];
    for (int i = 2; i <= n; i ++ )
      for (int j = 1; j <= i; j ++ )
        f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + a[i][j];
    
    int res = INF;
    for (int i = 1; i <= n; i ++ ) res = min(res, f[n][i]);
    return res;
  }
};