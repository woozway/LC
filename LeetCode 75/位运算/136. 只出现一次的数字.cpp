class Solution {
public:
  int singleNumber(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    int res = 0;
    for (int i = 0; i < n; i ++ ) res ^= a[i];
    return res;
  }
};