class Solution {
public:
  int searchInsert(vector<int>& nums, int target) {
    int n = nums.size();
    auto &a = nums;

    // 分成(<k, ..., <k), (>=k, ..., >=k)两部分
    int l = 0, r = n - 1;
    while (l < r) {
      int mid = l + r >> 1;
      if (a[mid] < target) l = mid + 1;
      else r = mid;
    }

    if (a[l] >= target) return l;
    return l + 1;
  }
};