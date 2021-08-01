// two pointers
// T=O(n)
// S=O(1)

class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    int lo = 0, hi = nums.size()-1;
    while (lo < hi) {
      int sum = nums[lo] + nums[hi];
      if (sum < target) lo++;
      else if (sum > target) hi--;
      else return vector<int>{nums[lo], nums[hi]};
    }
    return vector<int>{INT_MAX, INT_MAX};
  }
};
