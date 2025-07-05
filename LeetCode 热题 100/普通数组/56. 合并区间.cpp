const int INF = 2e9;

class Solution {
public:
  vector<vector<int>> merge(vector<vector<int>>& intervals) {
    auto &a = intervals;
    
    sort(a.begin(), a.end());
    
    vector<vector<int>> res;
    int st = -INF, ed = -INF; // 区间合并经典题，注意边界处理
    for (auto &seg : a)
      if (ed < seg[0]) {
        if (st != -INF) res.push_back({st, ed});
        st = seg[0], ed = seg[1];
      }
      else ed = max(ed, seg[1]);

    if (st != -INF) res.push_back({st, ed});
    return res;
  }
};