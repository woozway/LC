class Solution {
public:
  int equalPairs(vector<vector<int>>& grid) {
    int n = grid.size();
    auto &a = grid;

    map<vector<int>, int> M;
    for (int i = 0; i < n; i ++ ) {
      vector<int> t;
      for (int j = 0; j < n; j ++ ) t.push_back(a[i][j]);
      M[t] ++ ;
    }

    int res = 0;
    for (int i = 0; i < n; i ++ ) {
      vector<int> t;
      for (int j = 0; j < n; j ++ ) t.push_back(a[j][i]);
      if (M.count(t)) res += M[t];
    }
    return res;
  }
};