class Solution {
public:
  int singleNumber(vector<int>& nums) {
    int res = 0; // 统计每个比特位上的1的个数
    for (int i = 0; i < 32; i ++ ) {
      int cnt1 = 0;
      for (auto x : nums) cnt1 += x >> i & 1;
      res |= cnt1 % 3 << i;
    }
    return res;
  }
};