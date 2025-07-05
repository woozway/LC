class Solution {
public:
  vector<int> spiralOrder(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    auto &a = matrix;

    vector<int> res;
    int di[4] = {0, 1, 0, -1}, dj[4] = {1, 0, -1, 0}, k = 0;
    int rlim = n - 1, dlim = m - 1, llim = 0, ulim = 1; // right, down, left, up
    int x = 0, y = -1, cnt = 0;
    while (1) {
      while (y + dj[k] <= rlim)
        y += dj[k], res.push_back(a[x][y]), cnt ++ ;
      if (cnt >= m * n) break;
      rlim --;
      k = (k + 1) % 4;

      while (x + di[k] <= dlim)
        x += di[k], res.push_back(a[x][y]), cnt ++ ;
      if (cnt >= m * n) break;
      dlim -- ;
      k = (k + 1) % 4;

      while (y + dj[k] >= llim)
        y += dj[k], res.push_back(a[x][y]), cnt ++ ;
      if (cnt >= m * n) break;
      llim ++ ;
      k = (k + 1) % 4;

      while (x + di[k] >= ulim)
        x += di[k], res.push_back(a[x][y]), cnt ++ ;
      if (cnt >= m * n) break;
      ulim ++ ;
      k = (k + 1) % 4;
    }
    return res;
  }
};