typedef pair<int, int> PII;

class Solution {
  int res = 0;

  PII dfs(TreeNode *t) {
    if (!t) return {0, 0};
    
    auto [l1, r1] = dfs(t->left);
    auto [l2, r2] = dfs(t->right);
    res = max(res, r1 + 1);
    res = max(res, l2 + 1);

    return {r1 + 1, l2 + 1};
  }

public:
  int longestZigZag(TreeNode* root) {
    if (!root) return 0;
    dfs(root);
    return res - 1;
  }
};