class Solution {
  unordered_set<string> S;
  unordered_map<string, bool> M;

  bool dfs(string s) {
    if (M.count(s)) return M[s];
    if (S.count(s)) return M[s] = true;

    int n = s.size();
    string t = "";
    for (int i = 0; i < n; i ++ ) {
      t += s[i];
      if (S.count(t))
        if (!dfs(s.substr(i + 1))) M[s.substr(i + 1)] = false;
        else return M[s.substr(i + 1)] = true;
    }
    return M[s] = false;
  }

public:
  bool wordBreak(string s, vector<string>& wordDict) {
    for (auto x : wordDict) S.insert(x);

    return dfs(s);
  }
};