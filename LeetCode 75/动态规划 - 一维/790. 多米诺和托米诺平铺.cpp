typedef long long LL;
const int N = 1010, mod = 1e9 + 7;
// LL f[N];
LL f[N][1 << 2];

class Solution {
public:
  int numTilings(int n) {
    // if (n == 1) return 1;

    // memset(f, 0, sizeof f);

    // f[1] = f[0] = 1;
    // f[2] = 2;
    // for (int i = 3; i <= n; i ++ )
    //   f[i] = (f[i - 1] * 2 + f[i - 3]) % mod;
    
    // return f[n];

    f[0][3] = 1;
    for (int i = 1; i <= n; i++) {
      f[i][0] = f[i - 1][3];
      f[i][1] = (f[i - 1][0] + f[i - 1][2]) % mod;
      f[i][2] = (f[i - 1][0] + f[i - 1][1]) % mod;
      f[i][3] = (f[i - 1][0] + f[i - 1][1] + f[i - 1][2] + f[i - 1][3]) % mod;
    }
    return f[n][3];
  }
};