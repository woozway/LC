class Solution {
public:
  bool canJump(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    int res = 0;
    for (int i = 0; i < n; i ++ )
      if (i <= res) res = max(res, i + a[i]);

    return res >= n - 1;
  }
};