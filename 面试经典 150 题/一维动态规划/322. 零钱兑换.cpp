// 状态表示：f[i,j]表示a[1~i]个硬币面额中凑成数额j的硬币数，属性Min
// 状态计算：集合划分按最后一个硬币a_i的个数来划：k=0,1,2,...
// f[i, j]       = min(f[i - 1, j], f[i - 1, j - a_i] + 1, f[i - 1, j - a_i*2] + 2, ...)
// f[i, j - a_i] = min(             f[i - 1, j - a_i],     f[i - 1, j - a_i*2] + 1, ...)
// => f[i, j] = min(f[i - 1, j], f[i, j - a_i] + 1)
const int M = 15, N = 1e4 + 10;
// int f[M][N];
int f[N];
int a[N];

class Solution {
public:
  int coinChange(vector<int>& coins, int amount) {
    int n = coins.size();
    for (int i = 1; i <= n; i ++ ) a[i] = coins[i - 1];

    // memset(f, 0x3f, sizeof f);
    // f[0][0] = 0;
    // for (int i = 1; i <= n; i ++ )
    //   for (int j = 0; j <= amount; j ++ ) {
    //     f[i][j] = f[i - 1][j];
    //     if (j >= a[i]) f[i][j] = min(f[i][j], f[i][j - a[i]] + 1);
    //   }

    // if (f[n][amount] == 0x3f3f3f3f) return -1;
    // return f[n][amount];

    memset(f, 0x3f, sizeof f);
    f[0] = 0; // 滚动数组优化
    for (int i = 1; i <= n; i ++ )
      for (int j = a[i]; j <= amount; j ++ )
        f[j] = min(f[j], f[j - a[i]] + 1);
    
    if (f[amount] == 0x3f3f3f3f) return -1;
    return f[amount];
  }
};