// binary search II
// T=O(lgn)
// S=O(1)

class Solution {
public:
  int search(vector<int>& nums, int target) {
    int left = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    if (left != nums.size() && nums[left] == target) {
      int right = upper_bound(nums.begin(), nums.end(), target) - nums.begin();
      return right - left;
    }
    return 0;
  }
};
