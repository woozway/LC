class Solution {
public:
  vector<double> averageOfLevels(TreeNode* root) {
    if (!root) return {};

    vector<double> res;
    queue<TreeNode *> q;
    q.push(root);
    while (q.size()) {
      double s = 0;
      int n = q.size();
      for (int i = 0; i < n; i ++ ) {
        auto t = q.front(); q.pop();
        s += t->val;
        if (t->left) q.push(t->left);
        if (t->right) q.push(t->right);
      }
      res.push_back(s / n);
    }
    return res;
  }
};