unordered_map<char, int> M = {
  {'I', 1},
  {'V', 5},
  {'X', 10},
  {'L', 50}, 
  {'C', 100},
  {'D', 500},
  {'M', 1000},
};

class Solution {
public:
  int romanToInt(string s) {
    int res = 0;
    for (int i = 0; i + 1 < s.size(); i ++ ) {
      int x = M[s[i]], y = M[s[i + 1]];
      if (x < y) res += -x;
      else res += x;
    }
    return res + M[s.back()];
  }
};