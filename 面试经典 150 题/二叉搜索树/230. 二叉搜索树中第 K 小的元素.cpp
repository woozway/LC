class Solution {
  // int dfs(TreeNode *t) {
  //   if (!t) return 0;

  //   int l = dfs(t->left);
  //   int r = dfs(t->right);
  //   return l + r + 1;
  // }

public:
  int kthSmallest(TreeNode* root, int &k) {
    // if (!root) return 0;

    // auto &t = root;
    // int sl = dfs(t->left);
    // if (sl == k - 1) return t->val;
    // if (sl < k - 1) return kthSmallest(root->right, k - (sl + 1));
    // return kthSmallest(root->left, k);

    if (!root) return -1;

    auto &t = root;    
    int l = kthSmallest(t->left, k);
    if (l != -1) return l;
    if ( -- k == 0) return t->val;
    return kthSmallest(t->right, k); 
  }
};