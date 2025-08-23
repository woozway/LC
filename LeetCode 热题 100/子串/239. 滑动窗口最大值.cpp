const int N = 1e5 + 10;
int q[N], hh, tt; // 单调队列经典题，hh,tt分别是队列头尾指针

class Solution {
public:
  vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    auto &a = nums;
    int n = a.size();

    hh = 0, tt = -1;
    // 注意到如序列[1 3 -1 -3 5 3 6 7]，因为3>=1且3在1的右边，
    // 所以只要3在，1一定不是最大值的候选，可直接删去
    vector<int> res;
    for (int i = 0; i < n; i ++ ) {
      // 窗口右滑，将不再在窗口范围内的元素出队
      if (hh <= tt && q[hh] < i - k + 1) hh ++ ;
      // 如果队列不空，且队尾元素a[j]<=a[i]且j<i，那么可以删去j
      while (hh <= tt && a[q[tt]] <= a[i]) tt -- ;
      q[ ++ tt] = i;
      // 把>=当前元素的都撸掉了，处理后窗口中的元素是严格降序
      if (i >= k - 1) res.push_back(a[q[hh]]);
    }
    return res;
  }
};