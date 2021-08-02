// monotonic stack
// T=O(n)
// S=O(n)

class Solution {
public:
  int maxProfit(vector<int>& prices) {
    int maxprice = 0;
    stack<int> s;
    for (int i = 0; i < prices.size(); i++) {
      if (s.empty()) {
        s.push(prices[i]);
      } else {
        while (!s.empty() && s.top()>=prices[i]) {
          s.pop();
        }
        if (!s.empty() && s.top()<prices[i]) {
          maxprice = max(maxprice, prices[i]-s.top());
        } else {
          s.push(prices[i]);
        }
      }
    }
    return maxprice;
  }
};
