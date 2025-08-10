class Solution {
  TreeNode *dfs(vector<int> &a, int l, int r) {
    if (l > r) return nullptr;

    int mid = l + r >> 1;
    TreeNode *t = new TreeNode(a[mid]);
    t->left = dfs(a, l, mid - 1);
    t->right = dfs(a, mid + 1, r);
    return t;
  }

public:
  TreeNode* sortedArrayToBST(vector<int>& nums) {
    int n = nums.size();
    if (!n) return nullptr;

    auto &a = nums;
    return dfs(a, 0, n - 1);
  }
};