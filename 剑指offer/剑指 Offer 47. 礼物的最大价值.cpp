// dynamic programming, matrix
// T=O(m*n)
// S=O(m*n)

class Solution {
public:
  int maxValue(vector<vector<int>>& grid) {
    if (grid.size() == 0 || grid[0].size() == 0) return 0;
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    int runningSum = 0;
    for (int j = 0; j < n; j++) {
      runningSum += grid[0][j];
      dp[0][j] = runningSum;
    }
    runningSum = 0;
    for (int i = 0; i < m; i++) {
      runningSum += grid[i][0];
      dp[i][0] = runningSum;
    }
    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1]);
      }
    }
    return dp[m-1][n-1];
  }
};
