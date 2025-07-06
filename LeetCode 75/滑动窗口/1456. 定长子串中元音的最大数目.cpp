const int N = 128;
int a[N];

class Solution {
public:
  int maxVowels(string s, int k) {
    int n = s.size();

    memset(a, 0, sizeof a);

    int res = 0;
    for (int i = 0, j = 0; i < n; i ++ ) {
      if (i >= k) a[s[j ++ ]] -- ;
      a[s[i]] ++ ;

      int cnt = 0;
      for (auto x : "aeiou") cnt += a[x];
      res = max(res, cnt);
    }

    return res;
  }
};