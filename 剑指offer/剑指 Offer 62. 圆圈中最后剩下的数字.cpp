// recursion, Josephus problem
// T=O(n)
// S=O(n)

class Solution {
public:
  int lastRemaining(int n, int m) {
    return dp(n, m);
  }

  int dp(int n, int m) {
    if (n == 0) return 0;
    int x = dp(n-1, m);
    return (m + x) % n;
  }
};
