const int N = 4e4 + 10;
int son[N][26], cnt[N], idx;

class Trie {
public:
  Trie() {
    memset(son, 0, sizeof son);
    memset(cnt, 0, sizeof cnt);
    idx = 0;
  }
  
  void insert(string word) {
    int p = 0;
    for (int i = 0; i < word.size(); i ++ ) {
      int t = word[i] - 'a';
      if (!son[p][t]) son[p][t] = ++ idx;
      p = son[p][t];
    }
    cnt[p] ++ ;
  }
  
  bool search(string word) {
    int p = 0;
    for (int i = 0; i < word.size(); i ++ ) {
      int t = word[i] - 'a';
      if (!son[p][t]) return 0;
      p = son[p][t];
    }
    return cnt[p];
  }
  
  bool startsWith(string prefix) {
    int p = 0;
    for (int i = 0; i < prefix.size(); i ++ ) {
      int t = prefix[i] - 'a';
      if (!son[p][t]) return false;
      p = son[p][t];
    }
    return true;
  }
};