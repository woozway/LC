typedef long long LL;
const LL INF = 1ll << 60;

class Solution {
  bool dfs(TreeNode *t, LL minn, LL maxn) {
    if (!t) return true;
    if (t->val <= minn || t->val >= maxn) return false;
    
    bool l = dfs(t->left, minn, t->val);
    bool r = dfs(t->right, t->val, maxn);
    return l && r;
  }

public:
  bool isValidBST(TreeNode* root) {
    if (!root) return true;

    auto &t = root;
    bool l = dfs(t->left, -INF, t->val);
    bool r = dfs(t->right, t->val, INF);
    return l && r;
  }
};