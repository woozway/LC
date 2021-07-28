// divide and conquer, segment tree
// T=O(n)
// S=O(lgn)

class Solution {
public:
  struct Quartet {
    int iSum, lSum, rSum, mSum;
  };

  int maxSubArray(vector<int>& nums) {
    return getMaxSubSum(nums, 0, nums.size() - 1).mSum;
  }

  Quartet getMaxSubSum(vector<int>& nums, int lo, int hi) {
    if (lo >= hi) {
      return (Quartet) {nums[lo], nums[lo], nums[lo], nums[lo]};
    }
    int mid = lo + (hi-lo)/2;
    Quartet lSub = getMaxSubSum(nums, lo, mid);
    Quartet rSub = getMaxSubSum(nums, mid+1, hi);
    int iSum = lSub.iSum + rSub.iSum;
    int lSum = max(lSub.lSum, lSub.iSum+rSub.lSum);
    int rSum = max(rSub.rSum, rSub.iSum+lSub.rSum);
    int mSum = max(lSum, rSum); mSum = max(mSum, lSub.rSum+rSub.lSum); mSum = max(mSum, lSub.mSum); mSum = max(mSum, rSub.mSum);
    return (Quartet) {iSum, lSum, rSum, mSum};
  }
};
