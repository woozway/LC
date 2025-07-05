// 状态表示：f[i]表示a[0~i]结尾是i元素的子序列长度，属性：Max
// 状态计算：按照倒数第二个元素是k来划分，0<=k<i
// f[i] = max(f[i], f[k] + 1) if a[k]<a[i]
const int N = 2510;
// int f[N];
int q[N]; // q[i]表示长度为i的LIS的最小结尾数字；若j<i，则一定q[j]<q[i]（反证法）

class Solution {
public:
  int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    // for (int i = 0; i < n; i ++ ) {
    //   f[i] = 1;
    //   for (int j = 0; j < i; j ++ )
    //     if (a[j] < a[i]) f[i] = max(f[i], f[j] + 1);
    // }
    
    // int res = 0;
    // for (int i = 0; i < n; i ++ ) res = max(res, f[i]);
    // return res;

    q[0] = -2e9;
    int len = 0;
    for (int i = 0; i < n; i ++ ) {
      int l = 0, r = len;
      while (l < r) { // 二分找小于a[i]的最大的数p，分成(..., p), (...)两部分
        int mid = l + r + 1 >> 1;
        if (q[mid] < a[i]) l = mid;
        else r = mid - 1;
      }
      len = max(len, r + 1); // 更新len并在下一位置上放置新数
      q[r + 1] = a[i];
    }
    return len;
  }
};