typedef pair<int, int> PII;
const int N = 2e4 + 10;
int son[N][26], idx;

class Solution {
public:
  unordered_map<int, int> M1, M2; // M1: minMap, M2: maxMap

  void insert(string str, int num) {
    int p = 0;
    for (int i = 0; i < str.size(); i ++ ) {
      int t = str[i] - 'a';
      if (!son[p][t]) son[p][t] = ++ idx, M1[son[p][t]] = num;
      M2[son[p][t]] = num;
      p = son[p][t];
    }
  }

  PII query(string str) {
    int p = 0, a, b;
    for (int i = 0; i < str.size(); i ++ ) {
      int t = str[i] - 'a';
      if (!son[p][t]) return {-1, -1};
      a = M1[son[p][t]];
      b = M2[son[p][t]];
      p = son[p][t];
    }
    return {a, b};
  }

  vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
    memset(son, 0, sizeof son), idx = 0;

    auto &a = products;
    sort(a.begin(), a.end());
    
    for (int i = 0; i < a.size(); i ++ ) insert(a[i], i);

    vector<vector<string>> res;
    for (int i = 0; i < searchWord.size(); i ++ ) {
      vector<string> t;
      auto [l, r] = query(searchWord.substr(0, i + 1));
      for (int j = l; j <= min(l + 2, r) && l != -1; j ++ ) t.push_back(a[j]);
      res.push_back(t);
    }
    return res;
  }
};