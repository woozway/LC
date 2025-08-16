const int N = 2.5e5 + 10;
int son[N][26], cnt[N], idx;

class WordDictionary {
  bool dfs(int i, int p, string &w) {
    if (i == w.size()) return cnt[p];

    if (w[i] != '.') {
      int t = w[i] - 'a';
      if (!son[p][t]) return false;
      return dfs(i + 1, son[p][t], w);
    }
    else {
      for (int j = 0; j < 26; j ++ )
        if (son[p][j])
          if (dfs(i + 1, son[p][j], w)) return true;
      return false;
    }
  }

public:
  WordDictionary() {
    memset(son, 0, sizeof son);
    memset(cnt, 0, sizeof cnt);
    idx = 0;
  }
  
  void addWord(string word) {
    int p = 0;
    for (int i = 0; i < word.size(); i ++ ) {
      int t = word[i] - 'a';
      if (!son[p][t]) son[p][t] = ++ idx;
      p = son[p][t];
    }
    cnt[p] ++ ;
  }
  
  bool search(string word) {
    return dfs(0, 0, word);
  }
};