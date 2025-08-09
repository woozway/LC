class Solution {
  int res = 0;
  void dfs(TreeNode *t, int s) {
    if (!t) return;
    
    if (!t->left && !t->right) {
      res += s * 10 + t->val;
      return;
    }

    dfs(t->left, s * 10 + t->val);
    dfs(t->right, s * 10 + t->val);
  }

public:
  int sumNumbers(TreeNode* root) {
    dfs(root, 0);

    return res;
  }
};