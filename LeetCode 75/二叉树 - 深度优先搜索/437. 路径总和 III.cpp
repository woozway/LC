typedef long long LL;

class Solution {
  int target, res = 0;
  unordered_map<LL, int> M;

  void dfs(TreeNode *t, LL s) {
    if (!t) return;

    s += t->val;
    if (M.count(s - target)) res += M[s - target];

    M[s] ++ ;
    dfs(t->left, s);
    dfs(t->right, s);
    M[s] -- ;
  }

public:
  int pathSum(TreeNode* root, int targetSum) {
    if (!root) return 0;

    target = targetSum;
    M[0] = 1;
    dfs(root, 0);

    return res;
  }
};