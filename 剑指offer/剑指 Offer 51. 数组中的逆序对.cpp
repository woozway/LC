// mergesort, divide-and-conquer, recursion
// T=O(nlgn)
// S=O(n)

class Solution {
  int count = 0;

public:
  int reversePairs(vector<int>& nums) {
    if (nums.size() == 0) return 0;
    vector<int> tmp(nums.size());
    mergesort(0, nums.size()-1, nums, tmp);
    return count;
  }

  void mergesort(int lo, int hi, vector<int>& nums, vector<int>& tmp) {
    if (lo >= hi) return;
    int mid = lo + (hi-lo)/2;
    mergesort(lo, mid, nums, tmp);
    mergesort(mid+1, hi, nums, tmp);
    int i = lo, j = mid+1, index = lo;
    while (i<=mid && j<=hi) {
      if (nums[i] <= nums[j]) {
        tmp[index++] = nums[i++];
      } else {
        count += mid-i+1;
        tmp[index++] = nums[j++];
      }
    }
    while (i <= mid) tmp[index++] = nums[i++];
    while (j <= hi) tmp[index++] = nums[j++];
    for (int k = lo; k <= hi; k++) nums[k] = tmp[k];
  }
};
