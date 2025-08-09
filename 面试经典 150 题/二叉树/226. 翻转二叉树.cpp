class Solution {
public:
  TreeNode* invertTree(TreeNode* root) {
    if (!root) return nullptr;

    auto &t = root;
    TreeNode *l = invertTree(t->right);
    TreeNode *r = invertTree(t->left);
    
    t->left = l, t->right = r;
    return t;
  }
};