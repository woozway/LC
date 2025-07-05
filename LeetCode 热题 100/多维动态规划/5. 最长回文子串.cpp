const int N = 1010;
int f[N][N];

class Solution {
public:
  string longestPalindrome(string s) {
    int n = s.size();

    memset(f, 0, sizeof f);
    for (int i = 0; i < n; i ++ ) f[i][i] = 1;

    // 区间DP问题：st, len
    int start = 0, length = 1;
    for (int len = 2; len <= n; len ++ )
      for (int st = 0; st + len - 1 < n; st ++ )
        if (s[st] == s[st + len - 1])
          if (f[st + 1][st + len - 2] > 0 || len == 2) {
            f[st][st + len - 1] = f[st + 1][st + len - 2] + 2;
            if (len > length) start = st, length = len;
          }

    return s.substr(start, length);
  }
};