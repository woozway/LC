// 状态表示：f[i,j,0/1]表示前i天完成j次交易，不持有/持有时的利润；属性：Max
// 状态计算：按照当前是应该买入/卖出/不动来划分集合：
// f[i,j,0] = max(f[i-1,j,0], f[i-1,j-1,1] + a[i])
// f[i,j,1] = max(f[i-1,j,1], f[i-1,j,0] - a[i])
const int N = 1e5 + 10;
int a[N];
// int f[N][3][2];
int f[3][2];

class Solution {
public:
  int maxProfit(vector<int>& prices) {
    int n = prices.size();
    for (int i = 1; i <= n; i ++ ) a[i] = prices[i - 1];

    memset(f, -0x3f, sizeof f);
    // f[0][0][0] = 0;
    // for (int i = 1; i <= n; i ++ )
    //   for (int j = 0; j <= 2; j ++ ) {
    //     f[i][j][0] = f[i - 1][j][0];
    //     if (j >= 1) f[i][j][0] = max(f[i][j][0], f[i - 1][j - 1][1] + a[i]);
    //     f[i][j][1] = f[i - 1][j][1];
    //     f[i][j][1] = max(f[i][j][1], f[i - 1][j][0] - a[i]);
    //   }

    // return max({f[n][0][0], f[n][1][0], f[n][2][0]});

    // 滚动数组优化
    f[0][0] = 0;
    for (int i = 1; i <= n; i ++ )
      for (int j = 2; j >= 0; j -- ) {
        f[j][1] = max(f[j][1], f[j][0] - a[i]);
        if (j >= 1) f[j][0] = max(f[j][0], f[j - 1][1] + a[i]);
      }

    return max({f[0][0], f[1][0], f[2][0]});
  }
};