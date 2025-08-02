class Solution {
public:
  string longestCommonPrefix(vector<string>& strs) {
    string &s0 = strs[0];
    for (int i = 0; i < s0.size(); i ++ )
      for (string &s : strs)
        if (i == s.size() || s[i] != s0[i])
          return s0.substr(0, i);

    return s0;
  }
};