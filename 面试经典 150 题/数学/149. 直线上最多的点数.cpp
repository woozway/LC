const double INF = 1.0 / 0.0;

class Solution {
public:
  int maxPoints(vector<vector<int>>& points) {
    int n = points.size();

    int res = 0;
    for (int i = 0; i < n - 1; i ++ ) {
      auto &p = points[i];
      unordered_map<double, int> M;
      for (int j = i + 1; j < n; j ++ ) {
        auto &q = points[j];
        int dx = q[0] - p[0], dy = q[1] - p[1];
        double k = dx ? 1.0 * dy / dx : INF;
        res = max(res, ++ M[k]); // 这里没有算上 p 这个点，最后再加一
      }
    }
    return res + 1;
  }
};