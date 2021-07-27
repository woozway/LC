// recursion, fast-exp
// T=O(lgn)
// S=O(lgn)

class Solution {
public:
  double myPow(double x, long n) {
    if (x == 0) return 0;
    if (n == 0) return 1;
    if (n < 0) return 1 / myPow(x, -n);
    if (n % 2) return x * myPow(x, n-1);
    return myPow(x*x, n/2);
  }
};
