class Solution {
public:
  int findPeakElement(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    int l = 0, r = n - 1;
    while (l < r) {
      int mid = l + r >> 1;
      if (a[mid] < a[mid + 1]) l = mid + 1;
      else r = mid;
    }
    return l;
  }
};