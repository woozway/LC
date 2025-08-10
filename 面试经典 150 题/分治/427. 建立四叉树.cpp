class Solution {
  int n;
  vector<vector<int>> g;

  Node *dfs(int r0, int r1, int c0, int c1) {
    for (int i = r0; i <= r1; i ++ )
      for (int j = c0; j <= c1; j ++ )
        if (g[i][j] != g[r0][c0]) // 不是叶节点
          return new Node(
            1,
            false,
            dfs(r0, (r0 + r1) / 2, c0, (c0 + c1) / 2),
            dfs(r0, (r0 + r1) / 2, (c0 + c1) / 2 + 1, c1),
            dfs((r0 + r1) / 2 + 1, r1, c0, (c0 + c1) / 2),
            dfs((r0 + r1) / 2 + 1, r1, (c0 + c1) / 2 + 1, c1)
          );
    return new Node(g[r0][c0], true); // 是叶节点
  }

public:
  Node* construct(vector<vector<int>>& grid) {
    n = grid.size();
    g = grid;

    return dfs(0, n - 1, 0, n - 1);
  }
};