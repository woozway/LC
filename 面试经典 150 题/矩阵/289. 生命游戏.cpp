int dx[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[8] = {-1, 0, 1, 1, 1, 0, -1, -1};

class Solution {
public:
  void gameOfLife(vector<vector<int>>& board) {
    int n = board.size(), m = board[0].size();
    auto &a = board;

    for (int i = 0; i < n; i ++ )
      for (int j = 0; j < m; j ++ ) {
        int alive = 0;
        for (int k = 0; k < 8; k ++ ) {
          int u = i + dx[k], v = j + dy[k];
          if (u >= 0 && u < n && v >= 0 && v < m && abs(a[u][v]) == 1) alive ++ ;
        }

        if (a[i][j] == 1 && (alive < 2 || alive > 3)) a[i][j] = -1; // -1 代表这个细胞过去是活的现在死了
        if (a[i][j] == 0 && alive == 3) a[i][j] = 2; // 2 代表这个细胞过去是死的现在活了
      }

    // 更新board
    for (int i = 0; i < n; i ++ )
      for (int j = 0; j < m; j ++ )
        if (a[i][j] > 0) a[i][j] = 1;
        else a[i][j] = 0;
  }
};