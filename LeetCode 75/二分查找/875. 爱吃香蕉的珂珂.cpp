class Solution {
  int check(vector<int> &a, int v) {
    int res = 0;
    for (auto x : a)
      if (x % v) res += x / v + 1;
      else res += x / v;

    return res;
  }

public:
  int minEatingSpeed(vector<int>& piles, int h) {
    // 分成(>h, >h, >h), ..., (<=h, ...)两部分
    int l = 1, r = 1e9;
    while (l < r) {
      int mid = l + r >> 1;
      if (check(piles, mid) > h) l = mid + 1;
      else r = mid;
    }
    return l;
  }
};