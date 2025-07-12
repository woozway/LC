class Solution {
  void dfs(TreeNode *t, vector<int> &r) {
    if (!t) return;
    if (!t->left && !t->right) r.push_back(t->val);
    dfs(t->left, r);
    dfs(t->right, r);
  }

public:
  bool leafSimilar(TreeNode* root1, TreeNode* root2) {
    vector<int> res1, res2;

    dfs(root1, res1);
    dfs(root2, res2);

    return res1 == res2;
  }
};