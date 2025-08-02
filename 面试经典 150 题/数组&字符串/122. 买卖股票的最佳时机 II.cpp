class Solution {
public:
  int maxProfit(vector<int>& prices) {
    int n = prices.size();
    auto &a = prices;

    int res = 0;
    for (int i = 0; i < n - 1; i ++ )
      res += max(a[i + 1] - a[i], 0);

    return res;
  }
};