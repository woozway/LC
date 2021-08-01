// array
// T=O(1)
// S=O(1)

class Solution {
public:
  bool isStraight(vector<int>& nums) {
    unordered_set<int> s;
    int maxn = 0, minn = 14;
    for (auto& num : nums) {
      if (num == 0) continue;
      maxn = max(maxn, num);
      minn = min(minn, num);
      if (s.find(num) != s.end()) return false;
      s.insert(num);
    }
    return maxn-minn < 5;
  }
};

