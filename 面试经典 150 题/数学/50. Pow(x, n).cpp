typedef long long LL;

class Solution {
  double qmi(double a, LL b) {
    if (b == 0) return 1.0;

    double res = 1.0;
    while (b) {
      if (b & 1) res = res * a;
      a = a * a;
      b >>= 1;
    }
    return res;
  }

public:
  double myPow(double x, int n) {
    LL b = n;
    if (b > 0) return qmi(x, b);
    else return 1.0 / qmi(x, -b);
  }
};