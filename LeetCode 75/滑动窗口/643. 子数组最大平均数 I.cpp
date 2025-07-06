class Solution {
public:
  double findMaxAverage(vector<int>& nums, int k) {
    int n = nums.size();
    auto &a = nums;

    double res = -2e9, s = 0;
    for (int i = 0, j = 0; i < n; i ++ ) {
      if (i >= k) s -= a[j ++ ];
      s += a[i];
      if (i >= k - 1) res = max(res, s);
    }
    return res / k;
  }
};