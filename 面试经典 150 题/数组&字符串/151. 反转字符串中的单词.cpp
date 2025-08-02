class Solution {
public:
  string reverseWords(string s) {
    reverse(s.begin(), s.end());

    s += ' ';
    int n = s.size();
    
    string w, res;
    for (int i = 0; i < n; i ++ )
      if (s[i] != ' ') w += s[i];
      else {
        if (w.size()) {
          if (res.size()) res += ' ';
          reverse(w.begin(), w.end());
          res += w;
          w = "";
        }
      }

    return res;
  }
};