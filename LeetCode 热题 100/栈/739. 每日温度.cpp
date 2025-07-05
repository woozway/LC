const int N = 1e5 + 10;
int stk[N], tt; // 经典单调栈问题

class Solution {
public:
  vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    auto &a = temperatures;

    vector<int> res;
    for (int tt = 0, i = n - 1; ~i; i -- ) {
      while (tt && a[stk[tt]] <= a[i]) tt -- ;
      if (tt) res.push_back(stk[tt] - i);
      else res.push_back(0);
      stk[ ++ tt] = i;
    }

    reverse(res.begin(), res.end());
    return res;
  }
};