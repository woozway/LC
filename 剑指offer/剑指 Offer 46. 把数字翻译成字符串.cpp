// dynamic programming, string
// T=O(n)
// S=O(n)

class Solution {
public:
  int translateNum(int num) {
    if (num < 10) return 1;
    unordered_map<int, char> num2letter;
    for (int i = 0; i < 26; i++) {
      num2letter[i] = 'a' + i;
    }
    string s = to_string(num);
    int n = s.length();
    vector<int> dp(n+1, 0);
    dp[0] = dp[1] = 1;
    for (int i = 2; i <= n; i++) {
      if ((s[i-2]=='1' || s[i-2]=='2') && stoi(s.substr(i-2, 2))<26) {
        dp[i] += dp[i-2];
      }
      dp[i] += dp[i-1];
    }
    return dp[n];
  }
};
