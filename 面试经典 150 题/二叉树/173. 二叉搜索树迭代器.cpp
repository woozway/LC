class BSTIterator {
  TreeNode *t;
  stack<TreeNode *> stk;

public:
  BSTIterator(TreeNode* root) {
    t = root;
  }
  
  int next() {
    while (t) {
      stk.push(t);
      t = t->left;
    }
    t = stk.top(); stk.pop();
    int res = t->val;
    t = t->right;
    return res;
  }
  
  bool hasNext() {
    return t || stk.size();
  }
};