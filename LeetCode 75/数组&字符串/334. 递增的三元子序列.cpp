// const int N = 10;
// int q[N];
const int N = 5e5 + 10;
int a[N];
int s1[N], s2[N]; // s1和s2分别是从左往右最小的，从右往左最大的前缀和

class Solution {
public:
  bool increasingTriplet(vector<int>& nums) {
    int n = nums.size();
    // auto &a = nums;

    // // 在q中找到最后一个小于a[i]的数k的下标r：(..., k), (...)
    // q[0] = INT_MIN;
    // int len = 0; // 可参考最长上升子序列
    // for (int i = 0; i < n; i ++ ) {
    //   int l = 0, r = len;
    //   while (l < r) {
    //     int mid = l + r + 1 >> 1;
    //     if (q[mid] < a[i]) l = mid;
    //     else r = mid - 1;
    //   }
    //   q[r + 1] = a[i];
    //   len = max(len, r + 1);
    //   if (len >= 3) return true;
    // }
    // return false;

    for (int i = 1; i <= n; i ++ ) a[i] = nums[i - 1];

    for (int i = 0; i <= n; i ++ ) s1[i] = INT_MAX;
    for (int i = 1; i <= n; i ++ ) s1[i] = min(s1[i - 1], a[i]);

    for (int i = n + 1; i >= 1; i -- ) s2[i] = INT_MIN;
    for (int i = n; i >= 1; i -- ) s2[i] = max(s2[i + 1], a[i]);

    for (int i = 1; i <= n; i ++ )
      if (s1[i - 1] < a[i] && a[i] < s2[i + 1]) return true;
    return false;
  }
};