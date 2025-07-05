class Solution {
  string str;
  vector<vector<string>> res;
  vector<string> path;

  bool isPalindrome(string s, int l, int r) {
    for (int i = l, j = r; i < j; i ++, j -- )
      if (s[i] != s[j]) return false;
    return true;
  }

  void dfs(int u) {
    int n = str.size();
    if (u == n) {
      res.push_back(path);
      return;
    }

    for (int i = u; i < n; i ++ )
      if (isPalindrome(str, u, i)) {
        path.push_back(str.substr(u, i - u + 1));
        dfs(i + 1);
        path.pop_back();
      }
  }

public:
  vector<vector<string>> partition(string s) {
    str = s;
    dfs(0);
    return res;
  }
};