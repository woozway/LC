// 状态表示f[i, 0]：前i个元素中不选i元素时能偷到的价值，
// f[i, 1]，前i个元素中选i元素时能偷到的价值，属性：Max
// 状态计算：集合划分按照最后一个i元素选/不选
// f[i, 0] = max(f[i - 1, 0], f[i - 1, 1])
// f[i, 1] = f[i - 1,0] + a_i
const int N = 110;
int f[N][2];
int a[N];

class Solution {
public:
  int rob(vector<int>& nums) {
    int n = nums.size();
    for (int i = 1; i <= n; i ++ ) a[i] = nums[i - 1];

    memset(f, 0, sizeof f);
    for (int i = 1; i <= n; i ++ ) {
      f[i][0] = max(f[i - 1][0], f[i - 1][1]);
      f[i][1] = f[i - 1][0] + a[i];
    }
    return max(f[n][0], f[n][1]);
  }
};