class Solution {
  unordered_map<int, int> M;
  int maxdepth = 0;

  void dfs(TreeNode *t, int depth) {
    if (!t) return;

    if (!M.count(depth)) M[depth] = t->val;
    maxdepth = max(maxdepth, depth);
    dfs(t->right, depth + 1);
    dfs(t->left, depth + 1);
  }

public:
  vector<int> rightSideView(TreeNode* root) {
    if (!root) return {};

    auto &t = root;
    dfs(t, 1);
    
    vector<int> res;
    for (int i = 1; i <= maxdepth; i ++ ) res.push_back(M[i]);
    return res;
  }
};