// two pointers
// T=O(n)
// S=O(1)

class Solution {
public:
  vector<int> exchange(vector<int>& nums) {
    if (nums.size() == 0) {
      return nums;
    }
    int i = 0, j = nums.size()-1;
    while (true) {
      if (nums[i] % 2 == 1) i += 1;
      if (i > j) break;
      if (nums[j] % 2 == 0) j -= 1;
      if (i > j) break;
      swap(nums[i], nums[j]);
    }
    return nums;
  }
};
