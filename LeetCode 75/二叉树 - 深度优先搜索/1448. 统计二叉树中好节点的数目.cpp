const int INF = 0x3f3f3f3f;

class Solution {
  int res = 0;

  void dfs(TreeNode *t, int maxv) {
    if (!t) return;

    if (t->val >= maxv) res ++ ;
    
    maxv = max(maxv, t->val);
    dfs(t->left, maxv);
    dfs(t->right, maxv);
  }

public:
  int goodNodes(TreeNode* root) {
    dfs(root, -INF);
    return res;
  }
};