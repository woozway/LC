class Solution {
  int m, l;
  vector<vector<int>> res;
  vector<int> path;
  
  void dfs(int u) {
    if (u > m) {
      if (path.size() == l) res.push_back(path);
      return;
    }

    path.push_back(u);
    dfs(u + 1);
    path.pop_back();
    dfs(u + 1);
  }

public:
  vector<vector<int>> combine(int n, int k) {
    m = n, l = k;
    dfs(1);
    return res;
  }
};