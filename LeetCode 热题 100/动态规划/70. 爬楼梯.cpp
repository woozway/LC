// 状态表示f[i]：到达i阶的不同方法，属性：数量
// 状态计算：集合划分（按到达i阶的上一级台阶分）
// f[i] = f[i - 1] + f[i - 2]
const int N = 50;
int f[N];

class Solution {
public:
  int climbStairs(int n) {
    memset(f, 0, sizeof f);

    f[0] = f[1] = 1;
    for (int i = 2; i <= n; i ++ )
      f[i] = f[i - 1] + f[i - 2];
    return f[n];
  }
};