const int N = 1e5 + 10;
struct Range {
  int l, r;
  bool operator< (const Range &W)const {
    return r < W.r;
  }
} range[N];

// Acwing 908. 最大不相交区间数量
class Solution {
public:
  int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    int n = intervals.size();
    for (int i = 0; i < n; i ++ ) range[i] = {intervals[i][0], intervals[i][1]};

    sort(range, range + n);

    int res = 0, ed = -2e9;
    for (int i = 0; i < n; i ++ )
      if (range[i].l >= ed) {
        res ++ ;
        ed = range[i].r;
      }

    return n - res;
  }
};