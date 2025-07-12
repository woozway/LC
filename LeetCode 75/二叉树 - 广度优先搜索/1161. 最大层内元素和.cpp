class Solution {
public:
  int maxLevelSum(TreeNode* root) {
    int maxs = -2e9, layer = 0, res;
    queue<TreeNode *> q;

    q.push(root);
    while (q.size()) {
      layer ++ ;

      int n = q.size(), s = 0;
      for (int i = 0; i < n; i ++ ) {
        TreeNode *t = q.front(); q.pop();
        if (t->left) q.push(t->left);
        if (t->right) q.push(t->right);
        s += t->val;
      }
      
      if (s > maxs) maxs = s, res = layer;
    }
    return res;
  }
};