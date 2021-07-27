// simulation
// T=O(mn)
// S=O(mn)

class Solution {
public:
  vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> v;
    if (matrix.size() == 0 || matrix[0].size() == 0) {
      return v;
    }
    int m = matrix.size(), n = matrix[0].size();
    int delta = 0, left, right, up, down;
    while (true) {
      left = delta, right = n-1-delta;
      for (int i = left; i <= right; i++) v.push_back(matrix[delta][i]);
      if (v.size() >= m*n) break;
      up = delta+1, down = m-1-delta;
      for (int j = up; j <= down; j++) v.push_back(matrix[j][n-1-delta]);
      if (v.size() >= m*n) break;
      right = n-1-delta-1, left = delta;
      for (int i = right; i >= left; i--) v.push_back(matrix[m-1-delta][i]);
      if (v.size() >= m*n) break;
      down = m-1-delta-1, up = delta+1;
      for (int j = down; j >= up; j--) v.push_back(matrix[j][delta]);
      if (v.size() >= m*n) break;
      delta++;
    }
    return v;
  }
};
