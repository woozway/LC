class Solution {
public:
  int maxSubarraySumCircular(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    int s = 0, maxs = a[0], tmax = 0, mins = a[0], tmin = 0;
    for (int i = 0; i < n; i ++ ) {
      tmax = max(tmax + a[i], a[i]);
      maxs = max(maxs, tmax);
      tmin = min(tmin + a[i], a[i]);
      mins = min(mins, tmin);
      s += a[i];
    }

    if (maxs > 0) return max(maxs, s - mins);
    else return maxs;
  }
};