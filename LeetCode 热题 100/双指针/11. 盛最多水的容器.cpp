class Solution {
public:
  int maxArea(vector<int>& height) {
    int n = height.size();
    auto &a = height;

    // // O(n^2), TLE
    // int res = 0;
    // for (int i = 0; i < n; i ++ )
    //   for (int j = 0; j < i; j ++ )
    //     res = max(res, (i - j) * min(a[i], a[j]));
    // return res;

    // O(n)，双指针i,j指向两头，谁小移动谁，往可能盛更多水的方向交汇
    int res = 0;
    for (int i = 0, j = n - 1; i < n; i ++ ) {
      while (i < j && a[i] > a[j]) {
        res = max(res, (j - i) * min(a[i], a[j]));
        j -- ;
      }
      if (i < j) res = max(res, (j - i) * min(a[i], a[j]));
    }
    return res;
  }
};