class Solution {
public:
  bool containsNearbyDuplicate(vector<int>& nums, int k) {
    int n = nums.size();
    auto &a = nums;

    unordered_map<int, int> M;
    for (int i = 0; i < n; i ++ ) {
      if (M.count(a[i]))
        if (i - M[a[i]] <= k) return true;
      M[a[i]] = i;
    }
    return false;
  }
};