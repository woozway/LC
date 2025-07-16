typedef long long LL;
typedef pair<int, int> PII;

class Solution {
public:
  LL maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
    int n = nums1.size();
    auto &a = nums1, &b = nums2;

    vector<PII> idx;
    for (int i = 0; i < n; i ++ ) idx.push_back({-b[i], i});
    sort(idx.begin(), idx.end());

    priority_queue<int, vector<int>, greater<int>> q;
    LL s = 0;
    for (int i = 0; i < k; i ++ ) {
      auto [_, j] = idx[i];
      q.push(a[j]);
      s += a[j];
    }

    LL res = b[idx[k - 1].second] * s;
    for (int i = k; i < n; i ++ ) {
      auto [_, j] = idx[i];
      q.push(a[j]);
      s += a[j];

      s -= q.top(); q.pop();
      res = max(res, b[j] * s);
    }
    return res;
  }
};