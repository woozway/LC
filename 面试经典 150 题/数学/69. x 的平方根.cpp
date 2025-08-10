typedef long long LL;

class Solution {
public:
  int mySqrt(int x) {
    int l = 0, r = x;
    while (l < r) {
      int mid = (LL)l + r + 1 >> 1;
      if ((LL)mid * mid <= x) l = mid;
      else r = mid - 1;
    }
    return l;
  }
};