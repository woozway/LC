class Solution {
public:
  bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size(), n = matrix[0].size();
    auto &a = matrix;

    // 分成(<k, ..., <k), (>=k, ..., >=k)两部分
    int l = 0, r = m * n - 1;
    while (l < r) {
      int mid = l + r >> 1;
      if (a[mid / n][mid % n] < target) l = mid + 1;
      else r = mid;
    }

    return a[l / n][l % n] == target;
  }
};