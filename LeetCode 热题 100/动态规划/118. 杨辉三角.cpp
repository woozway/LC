const int N = 50;
int f[N][N];

class Solution {
public:
  vector<vector<int>> generate(int numRows) {
    memset(f, 0, sizeof f);

    vector<vector<int>> res;
    f[1][1] = 1;
    for (int i = 2; i <= numRows; i ++ )
      for (int j = 1; j <= i; j ++ )
        if (j == 1 || j == i) f[i][j] = 1;
        else f[i][j] = f[i - 1][j] + f[i - 1][j - 1];

    for (int i = 1; i <= numRows; i ++ ) {
      vector<int> a;
      for (int j = 1; j <= i; j ++ )
        a.push_back(f[i][j]);
      res.push_back(a);
    }

    return res;
  }
};