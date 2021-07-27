// dynamic programming
// T=O(n)
// S=O(n)

class Solution {
public:
  int cuttingRope(int n) {
    vector<long> dp(1001, 0);
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 2;
    dp[4] = 4;
    dp[5] = 6;
    dp[6] = 9;
    for(int i = 7; i <= n; i++){
      dp[i] = (dp[i-3] * 3) % 1000000007;
    }
    return dp[n];
  }
};
