class Solution {
public:
  bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
    int n = matrix.size(), m = matrix[0].size();
    if (!n || !m) return false;

    auto &a = matrix;

    int i = 0, j = m - 1;
    while (i < n && j >= 0)
      if (a[i][j] > target) j -- ;
      else if (a[i][j] < target) i ++ ;
      else return true;

    return false;
  }
};
