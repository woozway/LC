// dynamic programming
// T=O(n^2)
// S=O(n)

class Solution {
public:
  int cuttingRope(int n) {
    int dp[n+1];
    for (int i = 0; i < n+1; i++) {
      dp[i] = 1;
    }
    for (int i = 2; i < n+1; i++) {
      for (int j = 1; j < i; j++) {
        dp[i] = max(dp[i], j*(i-j));
        dp[i] = max(dp[i], j*dp[i-j]);
      }
    }
    return dp[n];
  }
};
