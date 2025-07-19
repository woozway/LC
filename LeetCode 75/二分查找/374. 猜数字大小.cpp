class Solution {
public:
  int guessNumber(int n) {
    // 分成 (...), (k, ...) 两部分
    int l = 1, r = n;
    while (l < r) {
      int mid = l + (r - l) / 2 + 1;
      if (guess(mid) >= 0) l = mid;
      else r = mid - 1;
    }
    return l;
  }
};