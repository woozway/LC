// recursion, hashing, tree
// T=O(n+m)
// S=O(n+m)

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
  unordered_map<int, TreeNode*> val2treeIndex;
public:
  bool isSubStructure(TreeNode* A, TreeNode* B) {
    dfs(A);
    if (B == nullptr) return false;
    if (val2treeIndex.find(B->val) == val2treeIndex.end()) return false;
    return check(val2treeIndex[B->val], B);
  }

  void dfs(TreeNode* node) {
    if (node == nullptr) {
      return;
    }
    val2treeIndex[node->val] = node;
    dfs(node->left);
    dfs(node->right);
  }

  bool check(TreeNode* rootA, TreeNode* rootB) {
    if (rootB == nullptr) return true;
    if (rootA == nullptr) return false;
    if (rootA->val != rootB->val) return false;
    return check(rootA->left, rootB->left) && check(rootA->right, rootB->right);
  }
};