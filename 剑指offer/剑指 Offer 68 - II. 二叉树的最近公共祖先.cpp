// tree, recursion
// T=O(n)
// S=O(height of tree)

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
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (root == nullptr) return root;
    if (root->val == p->val || root->val == q->val) return root;
    TreeNode* leftAns  = lowestCommonAncestor(root->left,  p, q);
    TreeNode* rightAns = lowestCommonAncestor(root->right, p, q);
    if (leftAns && rightAns) return root;
    else if (leftAns == nullptr) return rightAns;
    else return leftAns;
  }
};
