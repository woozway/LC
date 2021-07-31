// dfs, bfs, tree
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
  int maxDep = 0;

public:
  int maxDepth(TreeNode* root) {
    if (root == nullptr) return 0;
    dfs(root, 1);
    return maxDep;
  }

  void dfs(TreeNode* node, int depth) {
    if (node == nullptr) {
      return;
    }
    maxDep = max(maxDep, depth);
    dfs(node->left,  depth+1);
    dfs(node->right, depth+1);
  }
};
