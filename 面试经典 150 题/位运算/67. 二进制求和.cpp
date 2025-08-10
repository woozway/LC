class Solution {
public:
  string addBinary(string a, string b) {
    string res;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int n = max(a.size(), b.size()), c = 0;
    for (int i = 0; i < n; i ++ ) {
      if (i < a.size()) c += a[i] - '0';
      if (i < b.size()) c += b[i] - '0';

      if (c % 2) res.push_back('1');
      else res.push_back('0');
      c /= 2;
    }
    if (c) res.push_back('1');
    
    reverse(res.begin(), res.end());
    return res;
  }
};