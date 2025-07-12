class Solution {
  TreeNode *dfs(TreeNode *t, TreeNode *p, TreeNode *q) {
    if (!t) return nullptr;

    if (t == p || t == q) return t;

    TreeNode *l = dfs(t->left, p, q);
    TreeNode *r = dfs(t->right, p, q);
    if (l && r) return t;
    if (l) return l;
    return r;
  }

public:
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root) return nullptr;
    return dfs(root, p, q);
  }
};