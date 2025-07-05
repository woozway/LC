// 状态表示：f[i, j]表示前i个数字恰好组成j的方案，属性：1/0
// 状态计算：根据第i个是否选取来划分集合：不选：f[i, j] = f[i-1, j]；选：f[i, j] = f[i-1, j-a[i]] 
const int N = 210, M = 1e4 + 10;
// bool f[N][M];
bool f[M];
int a[N];

class Solution {
public:
  bool canPartition(vector<int>& nums) {
    int n = nums.size();
    
    for (int i = 1; i <= n; i ++ ) a[i] = nums[i - 1];

    int s = accumulate(a + 1, a + n + 1, 0);
    if (s % 2) return false;

    memset(f, 0, sizeof f);
    // f[0][0] = true;
    // for (int i = 1; i <= n; i ++ )
    //   for (int j = 0; j <= s / 2; j ++ ) {
    //     f[i][j] = f[i - 1][j];
    //     if (j >= a[i])
    //       f[i][j] = f[i][j] | f[i - 1][j - a[i]];
    //   }

    // return f[n][s / 2];

    f[0] = true;
    for (int i = 1; i <= n; i ++ )
      for (int j = s / 2; j >= a[i]; j -- )
        f[j] = f[j] | f[j - a[i]];

    return f[s / 2];
  }
};