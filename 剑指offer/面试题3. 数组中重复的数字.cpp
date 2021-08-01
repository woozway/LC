// hashing
// T=O(n)
// S=O(n)

class Solution {
public:
  int findRepeatNumber(vector<int>& nums) {
    unordered_map<int, int> um;
    for (auto i : nums) {
      um[i] += 1;
    }
    for (const auto &i : um) {
      if (i.second > 1) {
        return i.first;
      }
    }
    return nums.size();
  }
};
