class Solution {
public:
  vector<int> searchRange(vector<int>& nums, int target) {
    if (!nums.size()) return {-1, -1};

    auto &a = nums;
    int n = nums.size();

    vector<int> res;
    // 分成(...), (k, ...)两部分
    int l = 0, r = n - 1;
    while (l < r) {
      int mid = l + r >> 1;
      if (a[mid] < target) l = mid + 1;
      else r = mid;
    }

    if (a[l] != target) return {-1, -1};
    res.push_back(l);

    // 分成(..., k), (...)两部分
    l = 0, r = n - 1;
    while (l < r) {
      int mid = l + r + 1 >> 1;
      if (a[mid] <= target) l = mid;
      else r = mid - 1;
    }
    res.push_back(l);
    
    return res;
  }
};