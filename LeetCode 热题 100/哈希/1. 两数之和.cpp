class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    int n = nums.size();
    auto &a = nums;

    unordered_map<int, int> S;
    for (int i = 0; i < n; i ++ ) {
      if (S.count(target - a[i]))
        return {S[target - a[i]], i};
      S[a[i]] = i;
    }
    return {};
  }
};