const int N = 4e4 + 10;
int son[N][26], cnt[N], idx; // 每条边表示一个字符，每个节点是一个前缀

// trie[a][b]：a表示节点编号（和最多有多少个节点有关），b表示分叉
//      0
//    / | \  ..
//  a   b   c  ..
// ..  /|\  |\ ..
//    a b c
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
      if (!son[p][t]) son[p][t] = ++ idx; // 每个idx都对应一个独立前缀
      p = son[p][t];
    }
    cnt[p] ++ ; // cnt[i]是从Trie的根节点0走到i这个节点位置所对应的单词个数
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