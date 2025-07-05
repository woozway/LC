class Solution {
  vector<vector<int>> res;
  vector<int> path, a;
  
  void dfs(int u) {
    int n = a.size();
    if (u == n) {
      res.push_back(path);
      return;
    }

    dfs(u + 1);

    path.push_back(a[u]);
    dfs(u + 1);
    path.pop_back();
  }

public:
  vector<vector<int>> subsets(vector<int>& nums) {
    a = nums;
    dfs(0);
    return res;
  }
};