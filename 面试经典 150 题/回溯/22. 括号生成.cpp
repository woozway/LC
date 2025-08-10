class Solution {
  int m;
  vector<string> res;
  vector<char> path;

  void dfs(int u, int left, int right) {
    if (u == 2 * m) {
      string s;
      for (int i = 0; i < 2 * m; i ++ ) s += path[i];
      res.push_back(s);
      return;
    }

    if (left < m) {
      path.push_back('(');
      dfs(u + 1, left + 1, right);
      path.pop_back();
    }
    
    if (right < m && left > right) {
      path.push_back(')');
      dfs(u + 1, left, right + 1);
      path.pop_back();
    }
  }

public:
  vector<string> generateParenthesis(int n) {
    m = n;
    dfs(0, 0, 0);
    return res;
  }
};