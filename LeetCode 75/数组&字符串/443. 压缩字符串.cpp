class Solution {
public:
  int compress(vector<char>& chars) {
    int n = chars.size();
    auto &a = chars;

    int k = 0;
    for (int i = 0, j = 0; i < n; i ++ ) {
      j = max(j, i + 1);
      while (j < n && a[j] == a[i]) j ++ ;

      a[k ++ ] = a[i];
      
      int cnt = j - i;
      if (cnt > 1) {
        string s;
        while (cnt) {
          s += cnt % 10 + '0';
          cnt /= 10;
        }
        for (int i = s.size() - 1; ~i; i -- ) a[k ++ ] = s[i];
      }

      i = j - 1;
    }

    return k;
  }
};