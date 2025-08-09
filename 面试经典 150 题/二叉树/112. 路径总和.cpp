class Solution {
  bool res = false;
  int ts;

  void dfs(TreeNode *t, int s) {
    if (!t) return;
    if (!t->left && !t->right) {
      if (s + t->val == ts) res = true;
      return;
    }
    dfs(t->left, s + t->val);
    dfs(t->right, s + t->val);
  }

public:
  bool hasPathSum(TreeNode* root, int targetSum) {
    ts = targetSum;

    dfs(root, 0);
    
    return res;
  }
};