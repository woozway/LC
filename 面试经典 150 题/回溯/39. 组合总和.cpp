class Solution {
  vector<vector<int>> res;
  vector<int> path, a;

  void dfs(int u, int s) {
    int n = a.size();
    if (u == n) {
      if (path.size() && s == 0) res.push_back(path);
      return;
    }

    if (s < 0) return;

    if (s == 0) {
      if (path.size()) res.push_back(path);
      return;
    }

    path.push_back(a[u]);
    dfs(u, s - a[u]);
    path.pop_back();

    dfs(u + 1, s);
  }
public:
  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    a = candidates;
    dfs(0, target);
    return res;
  }
};