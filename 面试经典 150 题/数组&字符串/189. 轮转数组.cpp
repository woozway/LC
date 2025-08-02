class Solution {
public:
  void rotate(vector<int>& nums, int k) {
    int n = nums.size();
    auto &a = nums;

    k %= n; // 要先对n取余，否则越界或做无用功
    reverse(a.begin(), a.begin() + n - k);
    reverse(a.end() - k, a.end());
    reverse(a.begin(), a.end());
  }
};