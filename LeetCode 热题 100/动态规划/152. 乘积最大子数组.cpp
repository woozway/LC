// 状态表示：f[i, 0]表示以a_i结尾的子数组的乘积，属性：Max
//   f[i, 1]表示以a_i结尾的子数组的乘积，属性：Min
// 状态计算：集合划分按照是/否与上一个数连着形成子数组
//   f[i, 0] = max(f[i-1, 0] * a_i, f[i-1, 1] * a_i, a_i)
//   f[i, 1] = min(f[i-1, 0] * a_i, f[i-1, 1] * a_i, a_i)
const int N = 2e4 + 10;
int a[N];
int f[N][2];

class Solution {
public:
  int maxProduct(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    f[0][0] = f[0][1] = a[0];
    for (int i = 1; i < n; i ++ ) {
      f[i][0] = max({f[i - 1][0] * a[i], f[i - 1][1] * a[i], a[i]});
      f[i][1] = min({f[i - 1][0] * a[i], f[i - 1][1] * a[i], a[i]});
    }

    int res = INT_MIN;
    for (int i = 0; i < n; i ++ ) res = max(res, f[i][0]);
    return res;
  }
};