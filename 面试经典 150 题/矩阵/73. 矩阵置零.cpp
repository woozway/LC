class Solution {
public:
  void setZeroes(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    auto &a = matrix;

    unordered_set<int> rs, cs;
    for (int i = 0; i < m; i ++ )
      for (int j = 0; j < n; j ++ )
        if (!a[i][j]) rs.insert(i), cs.insert(j);

    for (int i = 0; i < m; i ++ )
      for (int j = 0; j < n; j ++ ) {
        if (rs.count(i)) a[i][j] = 0;
        if (cs.count(j)) a[i][j] = 0;
      }
  }
};