class Solution {
public:
  int maxSubArray(vector<int>& nums) {
    auto &a = nums;
    int n = a.size();

    int res = -2e9, s = 0;
    for (int i = 0; i < n; i ++ ) {
      s += a[i];
      res = max(res, s);
      if (s < 0) s = 0; // s<0对后续没增益，直接剔除归0
    }
    return res;
  }
};