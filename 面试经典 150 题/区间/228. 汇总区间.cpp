class Solution {
public:
  vector<string> summaryRanges(vector<int>& nums) {
    if (!nums.size()) return {};

    int n = nums.size();
    auto &a = nums;

    vector<int> v;
    for (int i = 0; i < n; i ++ )
      if (v.size() % 2 == 0) v.push_back(a[i]);
      else {
        int j = i;
        while (j < n && a[j] == a[j - 1] + 1) j ++ ;
        if (j < n) {
          v.push_back(a[j - 1]);
          i = j - 1;
        }
      }
    v.push_back(a[n - 1]);

    vector<string> res;
    for (int i = 0; i < v.size(); i += 2)
      if (v[i + 1] == v[i]) res.push_back(to_string(v[i]));
      else res.push_back(to_string(v[i]) + "->" + to_string(v[i + 1]));
    return res;
  }
};