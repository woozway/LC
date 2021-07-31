// dfs, tree
// T=O(n)
// S=O(n)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
  vector<int> inorder;
  int count = 0;

public:
  int kthLargest(TreeNode* root, int k) {
    dfs(root);
    return inorder[count-k];
  }

  void dfs(TreeNode* node) {
    if (node == nullptr) {
      return;
    }
    count += 1;
    dfs(node->left);
    inorder.push_back(node->val);
    dfs(node->right);
  }
};
