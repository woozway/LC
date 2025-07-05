// 状态表示：f[i]表示和为i的完全平方数的数量，属性：最少
// 状态计算：集合划分按照上一个为i-k^2，1<=k<sqrt(i)
// f[i] = min(f[i], f[i - k^2] + 1)
const int N = 1e4 + 10;
int f[N];

class Solution {
public:
  int numSquares(int n) {
    memset(f, 0x3f, sizeof f);

    f[0] = 0;
    for (int i = 1; i <= n; i ++ ) {
      int sq = sqrt(i);
      for (int j = 1; j <= sq; j ++ )
        f[i] = min(f[i], f[i - j * j] + 1);
    }
    return f[n];
  }
};