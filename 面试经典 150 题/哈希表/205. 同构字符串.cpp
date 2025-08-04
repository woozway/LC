class Solution {
public:
  bool isIsomorphic(string s, string t) {
    int n = s.size();
    unordered_map<char, char> s2t, t2s;

    for (int i = 0; i < n; i ++ ) {
      char x = s[i], y = t[i];
      
      if (s2t.count(x) && s2t[x] != y) return false;
      if (t2s.count(y) && t2s[y] != x) return false;

      s2t[x] = y, t2s[y] = x;
    }
    
    return true;
  }
};