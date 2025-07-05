class Solution {
public:
  int maxProfit(vector<int>& prices) {
    int n = prices.size();
    auto &a = prices;

    int res = 0, p = 0x3f3f3f3f;
    for (int i = 0; i < n; i ++ ) {
      res = max(res, a[i] - p);
      p = min(p, a[i]);
    }

    return res;
  }
};