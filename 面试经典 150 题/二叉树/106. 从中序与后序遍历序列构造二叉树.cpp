class Solution {
  vector<int> p, i;
  unordered_map<int, int> M;

  TreeNode *dfs(int pl, int pr, int il, int ir) {
    if (pl > pr) return nullptr;

    TreeNode *t = new TreeNode(p[pr]);
    // int j;
    // for (j = il; j <= ir; j ++ )
    //   if (i[j] == p[pr]) break;
    int j = M[p[pr]];
    
    int sl = j - 1 - il + 1;
    t->left = dfs(pl, pl + sl - 1, il, j - 1);
    t->right = dfs(pl + sl, pr - 1, j + 1, ir);
    return t;
  }

public:
  TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
    int n = postorder.size();
    if (!n) return nullptr;

    p = postorder, i = inorder;
    for (int j = 0; j < n; j ++ ) M[i[j]] = j;
    return dfs(0, n - 1, 0, n - 1);
  }
};