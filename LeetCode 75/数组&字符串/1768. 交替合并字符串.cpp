class Solution {
public:
  string mergeAlternately(string word1, string word2) {
    int n = word1.size(), m = word2.size();
    auto &a = word1, &b = word2;
    
    string res;
    for (int i = 0; i < n || i < m; i ++ ) {
      if (i < n) res += a[i];
      if (i < m) res += b[i];
    }
    return res;
  }
};