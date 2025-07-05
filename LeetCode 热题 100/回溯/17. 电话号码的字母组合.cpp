unordered_map<char, string> M = {
  {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, 
  {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
};

class Solution {
  string str;
  vector<char> v;
  vector<string> res;

  void dfs(int u) {
    int n = str.size();
    if (u == n) {
      string s;
      for (int i = 0; i < v.size(); i ++ ) s += v[i];
      res.push_back(s);
      return;
    }

    string ss = M[str[u]];
    for (int i = 0; i < ss.size(); i ++ ) {
      v.push_back(ss[i]);
      dfs(u + 1);
      v.pop_back();
    }
  }

public:
  vector<string> letterCombinations(string digits) {
    if (!digits.size()) return {};

    str = digits;
    dfs(0);
    return res;
  }
};