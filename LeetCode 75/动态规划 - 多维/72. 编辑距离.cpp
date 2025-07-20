// 状态表示：a. f[i,j]集合：字符串a[1~i]变成b[1~j]的最短编辑距离；b. 属性：Min
// 状态计算：集合划分（是否包含a[i], b[j]）；也可以按照增、删、替换3种操作来划分
//    00: f[i-1,j-1]+2,  01: f[i-1,j]+1, 
//    10: f[i,j-1]+1,    11: f[i-1,j-1] if a[i]==b[j] else f[i-1,j-1]+1
// 增：f[i,j-1]+1；删：f[i-1,j]+1；替换：f[i-1,j-1] if a[i]==b[j] else f[i-1,j-1]+1
const int N = 510;
char a[N], b[N];
int f[N][N];

class Solution {
public:
  int minDistance(string word1, string word2) {
    int n = word1.size(), m = word2.size();
    for (int i = 1; i <= n; i ++ ) a[i] = word1[i - 1];
    for (int i = 1; i <= m; i ++ ) b[i] = word2[i - 1];

    for (int i = 0; i <= m; i ++ ) f[0][i] = i;
    for (int i = 0; i <= n; i ++ ) f[i][0] = i;

    for (int i = 1; i <= n; i ++ )
      for (int j = 1; j <= m; j ++ ) {
        f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1);
        if (a[i] == b[j]) f[i][j] = min(f[i][j], f[i - 1][j - 1]);
        else f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1);
      }
    
    return f[n][m];
  }
};