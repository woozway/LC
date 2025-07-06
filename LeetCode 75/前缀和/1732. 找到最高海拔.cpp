class Solution {
public:
  int largestAltitude(vector<int>& gain) {
    int n = gain.size();
    auto &a = gain;

    int res = 0, s = 0;
    for (int i = 0; i < n; i ++ ) {
      s += a[i];
      res = max(res, s);
    }
    return res;
  }
};