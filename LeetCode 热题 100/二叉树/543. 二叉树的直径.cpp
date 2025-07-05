class Solution {
  int res = 0;

  int dfs(TreeNode *t) {
    if (!t) return 0;

    int l = dfs(t->left);
    int r = dfs(t->right);
    res = max(res, l + r);
    
    return max(l, r) + 1;
  }

public:
  int diameterOfBinaryTree(TreeNode* root) {
    dfs(root);
    return res;
  }
};