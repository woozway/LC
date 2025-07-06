class Solution {
public:
  int longestOnes(vector<int>& nums, int k) {
    int n = nums.size();
    auto &a = nums;
    
    // 滑动窗口[i~j]内的0的个数不能超过k个
    int res = 0, cnt0 = 0;
    for (int i = 0, j = 0; i < n; i ++ ) {
      if (a[i] == 0) cnt0 ++ ;
      while (j <= i && cnt0 > k) if (a[j ++ ] == 0) cnt0 -- ;
      if (j <= i) res = max(res, i - j + 1);
    }
    return res;
  }
};