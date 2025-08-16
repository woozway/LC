typedef tuple<int, int, int> TIII;

class Solution {
public:
  vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
    int m = nums1.size(), n = nums2.size();
    auto &a = nums1, &b = nums2;

    vector<vector<int>> res;
    priority_queue<TIII, vector<TIII>, greater<TIII>> q;
    for (int i = 0; i < min(m, k); i ++ ) q.push({a[i] + b[0], i, 0});

    while (res.size() < k) {
      auto [_, i, j] = q.top(); q.pop();
      res.push_back({a[i], b[j]});
      if (j + 1 < n) q.push({a[i] + b[j + 1], i, j + 1});
    }
    return res;
  }
};