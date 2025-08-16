typedef pair<int, int> PII;

class Solution {
public:
  int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
    int n = profits.size();

    vector<PII> a;
    for (int i = 0; i < n; i ++ ) a.push_back({capital[i], profits[i]});
    sort(a.begin(), a.end());

    priority_queue<int> q;
    for (int i = 0, j = 0; i < k; i ++ ) {
      while (j < n && a[j].first <= w) q.push(a[j ++ ].second);
      if (q.empty()) break;
      else w += q.top(), q.pop();
    }
    return w;
  }
};