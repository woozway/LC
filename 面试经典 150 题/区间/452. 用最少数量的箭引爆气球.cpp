typedef long long LL;
const int N = 1e5 + 10;
struct Range {
  int l, r;
  bool operator< (const Range &W)const {
    return r < W.r;
  }
} range[N];

// AcWing 905. 区间选点
class Solution {
public:
  int findMinArrowShots(vector<vector<int>>& points) {
    int n = points.size();
    for (int i = 0; i < n; i ++ ) range[i] = {points[i][0], points[i][1]};

    sort(range, range + n);

    int res = 0;
    LL ed = - (1l << 60);
    for (int i = 0; i < n; i ++ )
      if (range[i].l > ed) {
        res ++ ;
        ed = range[i].r;
      }

    return res;
  }
};