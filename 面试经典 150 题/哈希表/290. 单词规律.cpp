class Solution {
  vector<string> getWords(string s) {
    s += ' ';
    int n = s.size();
    
    vector<string> res;
    string w;
    for (int i = 0; i < n; i ++ )
      if (s[i] != ' ') w += s[i];
      else {
        if (w.size()) res.push_back(w), w = "";
      }
    return res;
  }

public:
  bool wordPattern(string pattern, string s) {
    int idx = 1;
    unordered_map<char, int> M1;
    vector<int> v1;
    for (int i = 0; i < pattern.size(); i ++ ) {
      if (!M1.count(pattern[i])) M1[pattern[i]] = idx ++ ;
      v1.push_back(M1[pattern[i]]);
    }

    auto t = getWords(s);
    
    idx = 1;
    unordered_map<string, int> M2;
    vector<int> v2;
    for (int i = 0; i < t.size(); i ++ ) {
      if (!M2.count(t[i])) M2[t[i]] = idx ++ ;
      v2.push_back(M2[t[i]]);
    }

    return v1 == v2;
  }
};