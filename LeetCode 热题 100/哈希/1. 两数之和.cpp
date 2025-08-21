class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    int n = nums.size();
    auto &a = nums;

    // 哈希表M存：已经看过的a[k]和其下标k的(k,v)映射
    unordered_map<int, int> M;
    for (int i = 0; i < n; i ++ ) {
      if (M.count(target - a[i])) return {M[target - a[i]], i};
      M[a[i]] = i;
    }
    return {};
  }
};