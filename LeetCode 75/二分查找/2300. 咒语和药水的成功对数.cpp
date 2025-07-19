typedef long long LL;

class Solution {
public:
  vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, LL success) {
    int n = spells.size(), m = potions.size();
    auto &s = spells, &p = potions;

    sort(p.begin(), p.end());
    
    // 找到第一个可以s*p > success的下标
    vector<int> res;
    for (int i = 0; i < n; i ++ ) {
      int l = 0, r = m - 1;
      while (l < r) {
        int mid = l + r >> 1;
        if ((LL)p[mid] * s[i] < success) l = mid + 1;
        else r = mid;
      }

      if ((LL)p[l] * s[i] >= success) res.push_back(m - 1 - l + 1);
      else res.push_back(0);
    }
    return res;
  }
};