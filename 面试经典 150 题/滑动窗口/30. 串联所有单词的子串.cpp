const int N = 128;
int as[N], ap[N];

class Solution {
  // 438. 找到字符串中所有字母异位词
  vector<int> findAnagrams(string s, string p) {
    int ns = s.size(), np = p.size();

    memset(as, 0, sizeof as), memset(ap, 0, sizeof ap);
    for (auto &c : p) ap[c] ++ ;

    vector<int> res;
    for (int i = 0, j = 0; i < ns; i ++ ) {
      as[s[i]] ++ ;
      while (j <= i && as[s[i]] > ap[s[i]]) as[s[j ++ ]] -- ;
      if (i - j + 1 == np) res.push_back(j);
    }
    return res;
  }

public:
  vector<int> findSubstring(string s, vector<string>& words) {
    int n = s.size(), m = words.size(), l = words[0].size();

    unordered_map<string, int> M;
    for (int i = 0; i < m; i ++ ) M[words[i]] ++ ;

    string p;
    for (int i = 0; i < m; i ++ ) p += words[i];

    auto a = findAnagrams(s, p);

    vector<int> res;
    for (int i = 0; i < a.size(); i ++ ) {
      string s1 = s.substr(a[i], m * l);

      unordered_map<string, int> M1;
      for (int j = 0; j < m; j ++ ) M1[s1.substr(j * l, l)] ++ ;

      if (M1 == M) res.push_back(a[i]);
    }
    return res;
  }
};