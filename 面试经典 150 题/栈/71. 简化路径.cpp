class Solution {
public:
  string simplifyPath(string path) {
    int n = path.size();
    auto &a = path;

    vector<string> stk;
    for (int i = 0; i < n; )
      if (a[i] == '/') i ++ ;
      else {
        int j = i;
        while (i < n && a[i] != '/') i ++ ;

        string s = a.substr(j, i - j);
        if (s == ".." && stk.size()) stk.pop_back();
        else if (s != "." && s != "..") stk.push_back(s);
      }
    if (!stk.size()) return "/";

    string res;
    for (string &s : stk) res += "/" + s;
    return res;
  }
};