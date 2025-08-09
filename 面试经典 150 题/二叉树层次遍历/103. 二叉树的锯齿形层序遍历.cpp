class Solution {
public:
  vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    if (!root) return {};

    vector<vector<int>> res;
    bool flag = false;
    queue<TreeNode *> q;
    q.push(root);
    while (q.size()) {
      vector<int> a;
      
      int n = q.size();
      while (n -- ) {
        auto t = q.front(); q.pop();
        a.push_back(t->val);

        if (t->left) q.push(t->left);
        if (t->right) q.push(t->right);
      }

      if (flag) reverse(a.begin(), a.end());
      flag = !flag;
      res.push_back(a);
    }
    return res;
  }
};