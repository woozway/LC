const int INF = 0x3f3f3f3f;

class Solution {
  int res = 0;

  void dfs(TreeNode *t, int maxn) {
    if (!t) return;

    if (t->val >= maxn) res ++ ;
    
    maxn = max(maxn, t->val);
    dfs(t->left, maxn);
    dfs(t->right, maxn);
  }

public:
  int goodNodes(TreeNode* root) {
    dfs(root, -INF);
    return res;
  }
};