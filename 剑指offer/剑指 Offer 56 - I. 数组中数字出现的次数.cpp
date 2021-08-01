// bit manipulation
// T=O(n)
// S=O(1)

class Solution {
public:
  vector<int> singleNumbers(vector<int>& nums) {
    int xor_sum = 0;
    for (auto& num : nums) {
      xor_sum ^= num;
    }
    int diff_bit = 1;
    while ((diff_bit & xor_sum) == 0) {
      diff_bit <<= 1;
    }
    int a = 0, b = 0;
    for (auto& num : nums) {
      if (num & diff_bit) {
        a ^= num;
      } else {
        b ^= num;
      }
    }
    return vector<int>{a, b};
  }
};
