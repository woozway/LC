// Boyer-Moore algo
// T=O(n)
// S=O(1)

class Solution {
public:
  int majorityElement(vector<int>& nums) {
    if (nums.size() == 0) {
      return INT_MAX;
    }
    int candidate = nums[0];
    int count = 1;
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] == candidate) {
        count += 1;
      } else {
        count -= 1;
      }
      if (count < 0) {
        candidate = nums[i];
        count = 1;
      }
    }
    return candidate;
  }
};
