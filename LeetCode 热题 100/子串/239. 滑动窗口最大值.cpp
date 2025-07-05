const int N = 1e5 + 10;
int q[N], hh, tt; // 单调队列经典题

class Solution {
public:
  vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    auto &a = nums;
    int n = a.size();

    vector<int> res;
    hh = 0, tt = -1;
    for (int i = 0; i < n; i ++ ) {
      if (hh <= tt && q[hh] < i - k + 1) hh ++ ;

      while (hh <= tt && a[q[tt]] <= a[i]) tt -- ;
      q[ ++ tt] = i;

      if (i >= k - 1) res.push_back(a[q[hh]]);
    }
    return res;
  }
};