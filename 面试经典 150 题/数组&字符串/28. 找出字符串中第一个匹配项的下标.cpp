const int N = 1e4 + 10;
char p[N], s[N];
int ne[N];

class Solution {
public:
  int strStr(string haystack, string needle) {
    int n = needle.size(), m = haystack.size();
    for (int i = 1; i <= n; i ++ ) p[i] = needle[i - 1];
    for (int i = 1; i <= m; i ++ ) s[i] = haystack[i - 1];

    for (int i = 2, j = 0; i <= n; i ++ ) {
      while (j && p[i] != p[j + 1]) j = ne[j];
      if (p[i] == p[j + 1]) j ++ ;
      ne[i] = j;
    }
    
    vector<int> res;
    for (int i = 1, j = 0; i <= m; i ++ ) {
      while (j && s[i] != p[j + 1]) j = ne[j];
      if (s[i] == p[j + 1]) j ++ ;
      if (j == n) {
        j = ne[j];
        res.push_back(i - n);
      }
    }

    if (res.size()) return res[0];
    else return -1;
  }
};