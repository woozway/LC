class Solution {
public:
  vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
    int n = candies.size();
    auto &a = candies;

    int m = 0;
    for (int i = 0; i < n; i ++ ) m = max(m, a[i]);

    vector<bool> res;
    for (int i = 0; i < n; i ++ )
      if (a[i] + extraCandies >= m) res.push_back(true);
      else res.push_back(false);

    return res;
  }
};