// 状态表示：f[i, 0/1]为到达i时，手上有/无股票的利润值；属性：Max
// 状态计算：按i天时是否持有股票来划分集合
// f[i, 0] = max(f[i - 1, 0], f[i - 1, 1] + a[i] - fee)
// f[i, 1] = max(f[i - 1, 1], f[i - 1][0] - a[i])
const int N = 5e4 + 10, INF = 0x3f3f3f3f;
int f[N][2];
int a[N];

class Solution {
public:
  int maxProfit(vector<int>& prices, int fee) {
    int n = prices.size();
    for (int i = 1; i <= n; i ++ ) a[i] = prices[i - 1];

    memset(f, 0, sizeof f);
    f[0][1] = -INF;

    for (int i = 1; i <= n; i ++ ) {
      f[i][0] = max(f[i - 1][0], f[i - 1][1] + a[i] - fee);
      f[i][1] = max(f[i - 1][1], f[i - 1][0] - a[i]);
    }
    
    return max(f[n][0], f[n][1]);
  }
};