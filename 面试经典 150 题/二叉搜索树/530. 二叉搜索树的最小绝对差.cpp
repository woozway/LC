typedef pair<int, int> PII;
const int INF = 0x3f3f3f3f;

class Solution {
  int res = INF;
  TreeNode *last = nullptr;

  void dfs(TreeNode *t) {
    if (!t) return;

    dfs(t->left);
    if (last) res = min(res, t->val - last->val);
    last = t;
    dfs(t->right);
  }

public:
  int getMinimumDifference(TreeNode* root) {
    dfs(root);
    return res;
  }
};