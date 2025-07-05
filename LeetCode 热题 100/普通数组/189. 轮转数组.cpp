class Solution {
public:
  void rotate(vector<int>& nums, int k) {
    int n = nums.size();
    auto &a = nums;

    k %= n; // 要先对n取余，否则越界或做无用功
    reverse(nums.begin(), nums.begin() + n - k);
    reverse(nums.end() - k, nums.end());
    reverse(nums.begin(), nums.end());
  }
};