const int N = 1e5 + 10;
int s[N];

class Solution {
public:
  int minSubArrayLen(int target, vector<int>& nums) {
    int n = nums.size();

    memset(s, 0, sizeof s);
    for (int i = 1; i <= n; i ++ ) s[i] = s[i - 1] + nums[i - 1];

    int res = n + 1;
    // O(n), 双指针
    for (int i = 0, j = 0; i <= n; i ++ )
      while (j <= i && s[i] - s[j] >= target) {
        res = min(res, i - j);
        j ++ ;
      }

    // // O(nlgn), 二分
    // for (int i = 0; i <= n; i ++ ) {
    //   int l = i, r = n;
    //   while (l < r) {
    //     int mid = l + r >> 1;
    //     if (s[mid] - s[i] < target) l = mid + 1;
    //     else r = mid;
    //   }
    //   if (s[l] - s[i] >= target) res = min(res, l - i);
    // }

    if (res == n + 1) return 0;
    else return res;
  }
};
