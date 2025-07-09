const int N = 1e5 + 10;
int stk[N], tt;

class Solution {
public:
  string removeStars(string s) {
    int n = s.size();

    tt = 0;
    for (int i = 0; i < n; i ++ )
      if (s[i] == '*') -- tt;
      else stk[ ++ tt] = s[i];

    string res;
    while (tt) res += stk[tt -- ];
    
    reverse(res.begin(), res.end());
    return res;
  }
};