// dfs, bfs
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
  unordered_map<int, vector<int>> layerList;
  int maxDepth = 0;

public:
  vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> v;
    if (root == nullptr) {
      return v;
    }
    dfs(root, 0);
    for (int i = 0; i <= maxDepth; i++) {
      v.push_back(layerList[i]);
    }
    return v;
  }

  void dfs(TreeNode* node, int depth) {
    if (node == nullptr) return;
    maxDepth = max(maxDepth, depth);
    if (layerList.find(depth) == layerList.end()) {
      layerList[depth] = *(new vector<int>());
    }
    layerList[depth].push_back(node->val);
    dfs(node->left,  depth+1);
    dfs(node->right, depth+1);
  }
};
