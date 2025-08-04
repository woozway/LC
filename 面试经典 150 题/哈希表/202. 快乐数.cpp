class Solution {
public:
  bool isHappy(int n) {
    unordered_set<int> S;
    S.insert(n);

    for ( ; ; ) {
      int res = 0;
      while (n) {
        int t = n % 10;
        res += t * t;
        n /= 10;
      }
      
      if (res == 1) break;
      
      if (S.count(res)) return false;

      S.insert(res);
      n = res;
    }
    return true;
  }
};