class Solution {
public:
  bool isSubsequence(string s, string t) {
    int ns = s.size(), nt = t.size();

    for (int i = 0, j = 0; i < ns; i ++ ) {
      while (j < nt && t[j] != s[i]) j ++ ;
      if (j == nt) return false;
      else j ++ ;
    }
    return true;
  }
};