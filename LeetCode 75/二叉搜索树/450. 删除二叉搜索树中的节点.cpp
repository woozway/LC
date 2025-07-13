class Solution {
public:
  TreeNode* deleteNode(TreeNode* root, int key) {
    auto &r = root;
    if (!r) return nullptr;
    if (r->val > key) {
      r->left = deleteNode(r->left, key);
      return root;
    }
    if (r->val < key) {
      r->right = deleteNode(r->right, key);
      return root;
    }

    if (!r->left && !r->right) return nullptr;
    if (!r->left) return r->right;
    if (!r->right) return r->left;
    
    TreeNode *t = r->right; // t找到右子树中最小的叶子节点
    while (t->left) t = t->left;
    r->right = deleteNode(r->right, t->val);
    
    t->left = r->left;
    t->right = r->right;
    return t;
  }
};