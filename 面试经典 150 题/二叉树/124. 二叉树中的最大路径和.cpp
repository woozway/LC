const int INF = 1e9;

class Solution {
  int res = -INF;

  int dfs(TreeNode *t) {
    if (!t) return 0;

    int l = max(0, dfs(t->left));
    int r = max(0, dfs(t->right));
    res = max(res, l + r + t->val);

    return max(l, r) + t->val;
  }

public:
  int maxPathSum(TreeNode* root) {
    dfs(root);
    return res;
  }
};