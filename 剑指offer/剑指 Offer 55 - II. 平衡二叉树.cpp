// tree, bottom-up recursion
// T=O(n)
// S=O(1)

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
  bool balanced = true;

public:
  bool isBalanced(TreeNode* root) {
    if (root == nullptr) return true;
    check(root);
    return balanced;
  }

  int check(TreeNode* node) {
    if (node == nullptr) return 0;
    int leftDepth  = check(node->left);
    int rightDepth = check(node->right);
    if (abs(leftDepth - rightDepth) > 1) {
      balanced = false;
    }
    return 1 + max(leftDepth, rightDepth);
  }
};