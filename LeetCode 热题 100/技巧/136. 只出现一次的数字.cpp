class Solution {
public:
  int singleNumber(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    // 2个相同数字异或^得0，任何数字异或0都是他本身
    int res = 0;
    for (int i = 0; i < n; i ++ ) res ^= a[i];
    return res;
  }
};