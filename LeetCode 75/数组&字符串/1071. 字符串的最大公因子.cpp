class Solution {
  int gcd(int a, int b) {
    return !b ? a : gcd(b, a % b);
  }

public:
  string gcdOfStrings(string str1, string str2) {
    int n = str1.size(), m = str2.size();
    auto &a = str1, &b = str2;

    // int d = gcd(n, m);
    // string lcs = a.substr(0, d);

    // string x;
    // for (int i = 0; i < n / d; i ++ ) x += lcs;
    // if (x != a) return "";

    // string y;
    // for (int i = 0; i < m / d; i ++ ) y += lcs;
    // if (y != b) return "";

    // return lcs;

    if (a + b != b + a) return "";
    return a.substr(0, gcd(n, m));
  }
};