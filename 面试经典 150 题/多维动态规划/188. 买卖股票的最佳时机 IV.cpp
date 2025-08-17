// 状态表示：f[i,j,0/1]表示前i天完成j次交易，不持有/持有时的利润；属性：Max
// 状态计算：按照当前是应该买入/卖出/不动来划分集合：
// f[i,j,0] = max(f[i-1,j,0], f[i-1,j-1,1] + a[i])
// f[i,j,1] = max(f[i-1,j,1], f[i-1,j,0] - a[i])
const int N = 1e3 + 10, INF = 0x3f3f3f3f;
int a[N];
// int f[N][110][2];
int f[110][2];

class Solution {
public:
  int maxProfit(int k, vector<int>& prices) {
    int n = prices.size();
    for (int i = 1; i <= n; i ++ ) a[i] = prices[i - 1];

    memset(f, -0x3f, sizeof f);
    // f[0][0][0] = 0;
    // for (int i = 1; i <= n; i ++ )
    //   for (int j = 0; j <= k; j ++ ) {
    //     f[i][j][0] = f[i - 1][j][0];
    //     if (j >= 1) f[i][j][0] = max(f[i][j][0], f[i - 1][j - 1][1] + a[i]);
    //     f[i][j][1] = f[i - 1][j][1];
    //     f[i][j][1] = max(f[i][j][1], f[i - 1][j][0] - a[i]);
    //   }

    // int res = -INF;
    // for (int i = 0; i <= k; i ++ ) res = max(res, f[n][i][0]);
    // return res;

    // 滚动数组优化
    f[0][0] = 0;
    for (int i = 1; i <= n; i ++ )
      for (int j = k; j >= 0; j -- ) {
        f[j][1] = max(f[j][1], f[j][0] - a[i]);
        if (j >= 1) f[j][0] = max(f[j][0], f[j - 1][1] + a[i]);
      }

    int res = -INF;
    for (int i = 0; i <= k; i ++ ) res = max(res, f[i][0]);
    return res;
  }
};