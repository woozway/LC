class Solution {
public:
  int findMin(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    // 分成：(...), (k, ...)两段递增序列
    int l = 0, r = n - 1;
    while (l < r) {
      int mid = l + r >> 1;
      if (a[mid] > a[r]) l = mid + 1; // 说明最小值在第二段
      else r = mid; // 说明最小值为a[mid]，或其左侧
    }

    return a[l];
  }
};