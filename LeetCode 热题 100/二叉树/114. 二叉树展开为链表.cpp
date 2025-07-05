class Solution {
  vector<TreeNode *> res;

  void dfs(TreeNode *t) {
    if (!t) return;

    res.push_back(t);
    dfs(t->left);
    dfs(t->right);
  }

public:
  void flatten(TreeNode* root) {
    if (!root) return;

    dfs(root);

    int n = res.size();
    for (int i = 0; i < n - 1; i ++ ) {
      res[i]->right = res[i + 1];
      res[i]->left = nullptr;
    }
  }
};