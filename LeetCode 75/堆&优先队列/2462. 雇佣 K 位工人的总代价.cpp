typedef long long LL;
typedef pair<int, int> PII;

class Solution {
public:
  LL totalCost(vector<int>& costs, int k, int candidates) {
    int n = costs.size();
    auto &a = costs;

    priority_queue<PII, vector<PII>, greater<PII>> q;
    int l = candidates - 1, r = n - candidates;
    if (l + 1 >= r) for (int i = 0; i < n; i ++ ) q.push({a[i], i});
    else {
      for (int i = 0; i <= l; i ++ ) q.push({a[i], i});
      for (int i = r; i < n; i ++ ) q.push({a[i], i});
    }

    LL res = 0;
    while (k -- ) {
      auto [c, idx] = q.top(); q.pop();
      res += c;
      if (l + 1 < r) {
        if (idx <= l) {
          l ++ ;
          q.push({a[l], l});
        }
        else {
          r -- ;
          q.push({a[r], r});
        }
      }
    }
    return res;
  }
};