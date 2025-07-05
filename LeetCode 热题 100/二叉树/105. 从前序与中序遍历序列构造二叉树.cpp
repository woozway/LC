class Solution {
  vector<int> p, i;
  unordered_map<int, int> M;

  TreeNode *dfs(int pl, int pr, int il, int ir) {
    if (pl > pr) return nullptr;

    TreeNode *t = new TreeNode(p[pl]);
    // int j;
    // for (j = il; j <= ir; j ++ )
    //   if (i[j] == p[pl]) break;
    int j = M[p[pl]];
    
    int sl = j - 1 - il + 1;
    t->left = dfs(pl + 1, pl + sl, il, j - 1);
    t->right = dfs(pl + sl + 1, pr, j + 1, ir);
    return t;
  }

public:
  TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    int n = preorder.size();
    if (!n) return nullptr;

    p = preorder, i = inorder;
    for (int j = 0; j < n; j ++ ) M[i[j]] = j;
    return dfs(0, n - 1, 0, n - 1);
  }
};