// recursion, regexp
// T=O((s+p)*2^(s+p/2)),
// S=O(s^2 + p^2)

class Solution {
public:
  bool isMatch(string s, string p) {
    if (s.empty() && p.empty()) return true;
    if (p.empty()) return false;
    if (s.empty()) {
      if (p.length() >= 2 && p[1] == '*') {
        return isMatch(s, p.substr(2));
      } else {
        return false;
      }
    }
    if (p[0] == '.' || p[0] == s[0]) {
      if (p.length() >= 2 && p[1] == '*') {
        return isMatch(s.substr(1), p) || isMatch(s, p.substr(2));
      } else {
        return isMatch(s.substr(1), p.substr(1));
      }
    } else {
      if (p.length() >= 2 && p[1] == '*') {
        return isMatch(s, p.substr(2));
      } else {
        return false;
      }
    }
  }
};
