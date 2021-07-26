// binary search tree
// T=O(n+m)
// S=O(1)

class Solution {
public:
  bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
    if (matrix.size() == 0 || matrix[0].size() == 0) {
      return false;
    }
    int n = matrix.size(), m = matrix[0].size();
    int r = 0, c = m - 1;
    while (r < n && c >= 0) {
      if (target < matrix[r][c]) {
        c -= 1;
      } else if (target > matrix[r][c]) {
        r += 1;
      } else {
        return true;
      }
    }
    return false;
  }
};
