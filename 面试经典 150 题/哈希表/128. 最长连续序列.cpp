class Solution {
public:
  int longestConsecutive(vector<int>& nums) {
    auto &a = nums;

    // sort(a.begin(), a.end());
    // a.erase(unique(a.begin(), a.end()), a.end());

    // unordered_map<int, int> M;
    // for (auto &x : a) {
    //   if (M.count(x - 1)) M[x] = M[x - 1];
    //   M[x] += 1;
    // }

    // int res = 0;
    // for (auto &x : a) res = max(res, M[x]);
    // return res;

    int res = 0;
    unordered_set<int> S(a.begin(), a.end());
    for (auto &x : S) {
      if (S.count(x + 1)) continue; // 先找到连续段的最右/左的数

      int y = x - 1;
      while (S.count(y)) y -- ;

      res = max(res, x - y);
    }
    return res;
  }
};