class Solution {
public:
  int findRepeatNumber(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;
    
    unordered_map<int, int> M;
    for (auto x : a) M[x] += 1;
  
    for (auto &[k, v] : M)
      if (v > 1) return k;
    return n;
  }
};
