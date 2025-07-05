// const int N = 1e4 + 10;
// int c[N];

class Solution {
public:
  int jump(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    // memset(c, 0x3f, sizeof c);
    // c[0] = 0;
    // for (int i = 0; i < n; i ++ )
    //   for (int j = 0; j <= a[i]; j ++ )
    //     if (i + j < n)
    //       c[i + j] = min(c[i + j], c[i] + 1);

    // return c[n - 1];

    int res = 0;
    int ed = 0, r = 0;
    for (int i = 0; i + 1 < n; i ++ ) {
      r = max(r, i + a[i]);
      if (i == ed) {
        ed = r;
        res ++ ;
      }
    }
    return res;
  }
};