// bottom-up recursion, tree
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
public:
  TreeNode* mirrorTree(TreeNode* root) {
    if (root == nullptr) return root;
    if (root->left == nullptr && root->right == nullptr) return root;
    root->left  = mirrorTree(root->left);
    root->right = mirrorTree(root->right);
    swap(root->left, root->right);
    return root;
  }
};
