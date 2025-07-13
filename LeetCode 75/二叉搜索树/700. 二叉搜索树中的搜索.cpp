class Solution {
  TreeNode *dfs(TreeNode *t, int v) {
    if (!t) return nullptr;

    if (t->val < v) return dfs(t->right, v);
    if (t->val > v) return dfs(t->left, v);
    return t;
  }

public:
  TreeNode* searchBST(TreeNode* root, int val) {
    return dfs(root, val);
  }
};