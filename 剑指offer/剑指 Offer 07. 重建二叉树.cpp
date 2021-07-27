// recursion
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
  unordered_map<int, int> inorderIndex;
public:
  TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    for (int i = 0; i < inorder.size(); i++) {
      inorderIndex[inorder[i]] = i;
    }
    return recursiveBuild(0, preorder.size()-1, 0, inorder.size()-1, preorder, inorder);
  }

  TreeNode* recursiveBuild(int preLeft, int preRight, int inLeft, int inRight, vector<int>& pre, vector<int>& in) {
    if (preLeft > preRight) {
      return nullptr;
    }
    int x = pre[preLeft];
    int index = inorderIndex[x];
    TreeNode *retNode = new TreeNode(x);
    int leftCount = index - inLeft;
    retNode->left = recursiveBuild(preLeft+1, preLeft+leftCount, inLeft, index-1, pre, in);
    int rightCount = inRight - index;
    retNode->right = recursiveBuild(preLeft+leftCount+1, preRight, index+1, inRight, pre, in);
    return retNode;
  }
};
