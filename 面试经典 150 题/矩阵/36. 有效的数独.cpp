class Solution {
public:
  bool isValidSudoku(vector<vector<char>>& board) {
    int r[9][9], c[9][9], b[3][3][9];
    memset(r, 0, sizeof(r)), memset(c, 0, sizeof(c)), memset(b, 0, sizeof(b));

    for (int i = 0; i < 9; i ++ )
      for (int j = 0; j < 9; j ++ ) {
        char ch = board[i][j];
        if (ch != '.') {
          int k = ch - '0' - 1;
          r[i][k] ++ ;
          c[j][k] ++ ;
          b[i / 3][j / 3][k] ++ ;
          if (r[i][k] > 1 || c[j][k] > 1 || b[i / 3][j / 3][k] > 1) return false;
        }
      }
    return true;
  }
};