class Solution {
public:
  bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size(), n = matrix[0].size();
    auto &a = matrix;

    // 以右上角为根节点的二叉搜素树
    int i = 0, j = n - 1;
    while (i < m && j >= 0) {
      if (a[i][j] < target) i ++ ;
      else if (a[i][j] > target) j -- ;
      else return true;
    }
    return false;
  }
};