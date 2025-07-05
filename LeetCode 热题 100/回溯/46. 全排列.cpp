const int N = 10;

class Solution {
  bool st[N];
  vector<vector<int>> res;
  vector<int> path, a;

  void dfs(int u) {
    int n = a.size();
    if (u == n) {
      res.push_back(path);
      return;
    }

    for (int i = 0; i < n; i ++ )
      if (!st[i]) {
        path.push_back(a[i]);
        st[i] = true;
        dfs(u + 1);
        st[i] = false;
        path.pop_back();
      }
  }

public:
  vector<vector<int>> permute(vector<int>& nums) {
    a = nums;
    dfs(0);
    return res;
  }
};