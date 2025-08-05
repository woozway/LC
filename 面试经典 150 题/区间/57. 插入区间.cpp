const int INF = 2e9;

class Solution {
  vector<vector<int>> merge(vector<vector<int>>& intervals) {
    auto &a = intervals;
    
    // sort(a.begin(), a.end());
    
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

public:
  vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    int n = intervals.size();
    auto &a = intervals;

    vector<vector<int>> res;

    int i = 0;
    while (i < a.size())
      if (a[i][0] >= newInterval[0]) break;
      else res.push_back(a[i ++ ]);
    res.push_back(newInterval);

    while (i < a.size()) res.push_back(a[i ++ ]);

    return merge(res);
  }
};