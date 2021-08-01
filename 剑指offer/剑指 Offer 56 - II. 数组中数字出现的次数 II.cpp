// bit manipulation
// T=O(n)
// S=O(1)

class Solution {
public:
  int singleNumber(vector<int>& nums) {
    vector<int> oneCounts(32, 0);
    for (int i = 0; i < 32; i++) {
      for (auto& num : nums) {
        oneCounts[i] += (num & (1<<i) ? 1 : 0);
      }
    }
    int ans = 0;
    for (int i = 31; i >= 0; i--) {
      ans = ans*2 + oneCounts[i]%3;
    }
    return ans;
  }
};
