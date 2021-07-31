// dfs, bfs, reverse
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
  unordered_map<int, vector<int>> layer2list;
  int maxDepth = -1;

public:
  vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> v;
    dfs(root, 0);
    for (int i = 0; i <= maxDepth; i++) {
      if (i % 2 == 1) {
        reverse(layer2list[i].begin(), layer2list[i].end());
      }
      v.push_back(layer2list[i]);
    }
    return v;
  }

  void dfs(TreeNode* node, int depth) {
    if (node == nullptr) {
      return;
    }
    maxDepth = max(maxDepth, depth);
    if (layer2list.find(depth) == layer2list.end()) {
      layer2list[depth] = *(new vector<int>());
    }
    layer2list[depth].push_back(node->val);
    dfs(node->left,  depth+1);
    dfs(node->right, depth+1);
  }
};
