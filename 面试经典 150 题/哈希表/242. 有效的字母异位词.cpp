const int N = 128 + 10;
int as[N], at[N];

class Solution {
public:
  bool isAnagram(string s, string t) {
    memset(as, 0, sizeof as), memset(at, 0, sizeof at);
    
    for (char c : s) as[c] ++ ;
    for (char c : t) at[c] ++ ;

    for (int i = 0; i < N; i ++ )
      if (as[i] != at[i]) return false;
    return true;
  }
};