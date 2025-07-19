class Solution {
  int kk, nn;
  vector<int> path;
  vector<vector<int>> res;

  void dfs(int i, int s, int st) {
    if (i >= kk) {
      if (s == nn)
        res.push_back(path);
      return;
    }

    // 从数字 st 开始选，下一层从 st+1 开始选，保证不出现重复
    for (int j = st; j <= 9; j ++ ) {
      path.push_back(j);
      dfs(i + 1, s + j, j + 1);
      path.pop_back();
    }
  }

public:
  vector<vector<int>> combinationSum3(int k, int n) {
    kk = k, nn = n;
    dfs(0, 0, 1);
    return res;
  }
};