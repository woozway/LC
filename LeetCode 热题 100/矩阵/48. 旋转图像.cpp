class Solution {
public:
  void rotate(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    auto &a = matrix;
    
    // 转置：(i, j) -> (j, i)；每行逆序：(i, j) -> (i, n-1-j)
    // 顺时针：(i, j) -> (j, n-1-i)，分解为两步：1. 转置  2. 每行逆序
    // 逆时针：(i, j) -> (n-1-j, i)同理，分两步：1. 每行逆序  2. 转置
    for (int i = 0; i < m; i ++ )
      for (int j = 0; j <= i; j ++ )
        swap(a[i][j], a[j][i]);
    
    for (int i = 0; i < m; i ++ )
      reverse(a[i].begin(), a[i].end());
  }
};