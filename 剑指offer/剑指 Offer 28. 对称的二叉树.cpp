// recursion, tree
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
  bool isSymmetric(TreeNode* root) {
    if (root == nullptr) return true;
    return check(root, root);
  }

  bool check(TreeNode* rootA, TreeNode* rootB) {
    if (rootA == nullptr && rootB == nullptr) return true;
    if (rootA == nullptr) return false;
    if (rootB == nullptr) return false;
    if (rootA->val != rootB->val) return false;
    return check(rootA->left, rootB->right) && check(rootA->right, rootB->left);
  }
};
