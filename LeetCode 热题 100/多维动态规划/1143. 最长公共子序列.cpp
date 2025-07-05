// 状态表示：f[i,j]表示前i个a和前j个b的公共子序列长度；属性：Max
// 状态计算：按a[i]和b[j]是否选择来划分集合：00,01,10,11
// 00: f[i,j] = f[i-1,j-1], 10: f[i,j] = f[i-1,j]
// 01: f[i,j] = f[i,j-1], 11: f[i,j] = f[i-1,j-1] + 1 if a[i]==b[j] else 0
const int N = 1010;
int f[N][N];
char a[N], b[N];

class Solution {
public:
  int longestCommonSubsequence(string text1, string text2) {
    int n = text1.size(), m = text2.size();
    for (int i = 1; i <= n; i ++ ) a[i] = text1[i - 1];
    for (int i = 1; i <= m; i ++ ) b[i] = text2[i - 1];

    memset(f, 0, sizeof f);
    for (int i = 1; i <= n; i ++ )
      for (int j = 1; j <= m; j ++ ) {
        f[i][j] = max(f[i - 1][j], f[i][j - 1]);
        if (a[i] == b[j]) f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1);
      }

    return f[n][m];
  }
};