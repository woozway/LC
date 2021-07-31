// dfs, bfs, tree
// T=O(n^2)
// S=O(1)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
  vector<vector<int>> ans;
  int targetSum;

public:
  vector<vector<int>> pathSum(TreeNode* root, int target) {
    targetSum = target;
    vector<int> tmplist;
    backtrack(root, tmplist, 0);
    return ans;
  }

  void backtrack(TreeNode* node, vector<int>& tmplist, int tmpSum) {
    if (node == nullptr) {
      return;
    }
    tmplist.push_back(node->val);
    tmpSum += node->val;
    if (node->left == nullptr && node->right == nullptr) {
      if (tmpSum == targetSum) {
        ans.push_back(vector<int>(tmplist));
      }
      tmplist.pop_back();
      tmpSum -= node->val;
      return;
    }
    backtrack(node->left,  tmplist, tmpSum);
    backtrack(node->right, tmplist, tmpSum);
    tmplist.pop_back();
    tmpSum -= node->val;
  }
};