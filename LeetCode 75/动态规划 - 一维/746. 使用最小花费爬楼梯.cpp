// 状态表示：f[i]为爬到台阶i的费用；属性：Min
// 状态计算：按照到达台阶i的上一个台阶划分集合
// f[i] = min(f[i - 1] + a[i - 1], f[i - 2] + a[i - 2])
const int N = 1010;
int f[N];

class Solution {
public:
  int minCostClimbingStairs(vector<int>& cost) {
    int n = cost.size();
    auto &a = cost;

    memset(f, 0, sizeof f);

    for (int i = 2; i <= n; i ++ )
      f[i] = min(f[i - 1] + a[i - 1], f[i - 2] + a[i - 2]);

    return f[n];
  }
};