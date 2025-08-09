class Solution {
  int res = 0;

  void dfs(TreeNode *t, int depth) {
    if (!t) return;

    res = max(res, depth);
    dfs(t->left, depth + 1);
    dfs(t->right, depth + 1);
  }
  
public:
  int maxDepth(TreeNode* root) {
    dfs(root, 1);
    return res;
  }
};