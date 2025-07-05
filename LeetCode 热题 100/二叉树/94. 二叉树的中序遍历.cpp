class Solution {
  // vector<int> res;

  // void dfs(TreeNode *t) {
  //   if (!t) return;

  //   dfs(t->left);
  //   res.push_back(t->val);
  //   dfs(t->right);
  // }

public:
  vector<int> inorderTraversal(TreeNode* root) {
    // dfs(root);
    // return res;

    vector<int> res;
    stack<TreeNode *> stk;
    auto &t = root;
    while (t || stk.size()) {
      while (t) {
        stk.push(t);
        t = t->left;
      }
      t = stk.top(); stk.pop();
      res.push_back(t->val);
      t = t->right;
    }
    return res;
  }
};