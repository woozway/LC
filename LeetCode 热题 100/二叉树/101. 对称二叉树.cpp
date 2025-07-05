class Solution {
  bool dfs(TreeNode *a, TreeNode *b) {
    if (!a && !b) return true;
    if (!a && b) return false;
    if (a && !b) return false;
    if (a->val != b->val) return false;
    return dfs(a->left, b->right) && dfs(a->right, b->left);
  }

public:
  bool isSymmetric(TreeNode* root) {
    return dfs(root, root);
  }
};