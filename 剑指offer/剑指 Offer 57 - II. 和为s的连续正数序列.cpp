// sliding window
// T=O(n)
// S=O(n)

class Solution {
public:
  vector<vector<int>> findContinuousSequence(int target) {
    vector<int> nums;
    for (int i = 1; i <= target; i++) {
      nums.push_back(i);
    }
    int n = nums.size();
    vector<vector<int>> ans;
    int lo = 0, hi = 0, runningSum = 0;
    while (lo < n) {
      if (runningSum > target) {
        runningSum -= nums[lo++];
      } else if (runningSum < target) {
        runningSum += nums[hi++];
      } else {
        if (hi-lo >= 2) {
          vector<int> tmp;
          for (int i = lo; i < hi; i++) {
            tmp.push_back(nums[i]);
          }
          ans.push_back(tmp);
        }
        runningSum -= nums[lo++];
      }
    }
    return ans;
  }
};
