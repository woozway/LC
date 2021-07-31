// binary search I
// T=O(lgn)
// S=O(1)

class Solution {
public:
  int missingNumber(vector<int>& nums) {
    int lo = 0, hi = nums.size()-1;
    while (lo <= hi) {
      int mid = lo + (hi-lo)/2;
      if (nums[mid] == mid) {
        lo = mid + 1;
      } else {
        hi = mid - 1;
      }
    }
    return lo;
  }
};