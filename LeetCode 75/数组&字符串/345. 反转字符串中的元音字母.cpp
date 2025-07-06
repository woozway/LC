class Solution {
public:
  string reverseVowels(string s) {
    unordered_set<char> S;
    for (auto &c : "AaEeIiOoUu") S.insert(c);

    int n = s.size();
    // vector<char> a;
    // for (int i = 0; i < n; i ++ )
    //   if (S.count(s[i])) a.push_back(s[i]);
    
    // reverse(a.begin(), a.end());

    // for (int i = 0, j = 0; i < n; i ++ )
    //   if (S.count(s[i])) s[i] = a[j ++ ];

    for (int i = 0, j = n - 1; i < n; i ++ ) {
      if (!S.count(s[i])) continue;

      while (j >= i && !S.count(s[j])) j -- ;
      if (j >= i) swap(s[i], s[j -- ]);
    }

    return s;
  }
};