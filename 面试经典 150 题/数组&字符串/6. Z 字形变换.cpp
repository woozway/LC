const int N = 1010;
char g[N][N];

class Solution {
public:
  string convert(string s, int numRows) {
    if (numRows == 1) return s;
    
    memset(g, '*', sizeof g);
    for (int i = 0, j = 0, k = 0; ; ) {
      while (i < s.size() && j < numRows) g[j ++ ][k] = s[i ++ ];
      if (i >= s.size()) break;
      i -- , j -- ;

      while (i < s.size() && j >= 0) g[j -- ][k ++ ] = s[i ++ ];
      if (i >= s.size()) break;
      i -- , j ++ , k -- ;
    }

    string res;
    for (int i = 0; i < N; i ++ )
      for (int j = 0; j < N; j ++ )
        if (g[i][j] != '*') res += g[i][j];

    return res;
  }
};