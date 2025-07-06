// const int N = 1e5 + 10;
// int a[N], s1[N], s2[N];

class Solution {
public:
  int longestSubarray(vector<int>& nums) {
    int n = nums.size();
    // for (int i = 1; i <= n; i ++ ) a[i] = nums[i - 1];

    // memset(s1, 0, sizeof s1); memset(s2, 0, sizeof s2);
    // for (int i = 1; i <= n; i ++ ) if (a[i] == 1) s1[i] = s1[i - 1] + 1;
    // for (int i = n; i >= 1; i -- ) if (a[i] == 1) s2[i] = s2[i + 1] + 1;

    // int res = 0;
    // for (int i = 1; i <= n; i ++ ) res = max(res, s1[i - 1] + s2[i + 1]);
    // return res;

    auto &a = nums;
    // 滑动窗口[i~j]内的0的个数不能超过1个
    int res = 0, cnt0 = 0;
    for (int i = 0, j = 0; i < n; i ++ ) {
      if (a[i] == 0) cnt0 ++ ;
      while (j <= i && cnt0 > 1) if (a[j ++ ] == 0) cnt0 -- ;
      if (j <= i) res = max(res, i - j + 1);
    }
    return res - 1; // 必须删掉一个元素
  }
};