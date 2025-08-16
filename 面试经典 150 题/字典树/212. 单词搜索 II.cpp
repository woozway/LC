const int N = 3e4 + 10;
int son[N][26], cnt[N], idx;
vector<vector<char>> g;
int m, n;
bool st[15][15];

class Solution {
  unordered_set<string> S;
  vector<char> path;
  vector<string> res;
  int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

  void dfs(int i, int j, int p) {
    if (cnt[p]) {
      string r;
      for (int k = 0; k < path.size(); k ++ ) r += path[k];
      if (r.size()) S.insert(r);
    }

    for (int k = 0; k < 4; k ++ ) {
      int x = i + dx[k], y = j + dy[k];
      if (x >= 0 && x < m && y >= 0 && y < n && !st[x][y]) {
        int t = g[x][y] - 'a';
        if (!son[p][t]) continue;
        path.push_back(g[x][y]), st[x][y] = true;
        dfs(x, y, son[p][t]);
        path.pop_back(), st[x][y] = false;
      }
    }
  }

  void insert(string &str) {
    int p = 0;
    for (int i = 0; i < str.size(); i ++ ) {
      int t = str[i] - 'a';
      if (!son[p][t]) son[p][t] = ++ idx;
      p = son[p][t];
    }
    cnt[p] ++ ;
  }

public:
  vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    m = board.size(), n = board[0].size(), g = board;

    memset(son, 0, sizeof son), memset(cnt, 0, sizeof cnt), memset(st, 0, sizeof st), idx = 0;
    for (auto &w : words) insert(w);

    for (int i = 0; i < m; i ++ )
      for (int j = 0; j < n; j ++ ) {
        int t = g[i][j] - 'a';
        if (!son[0][t]) continue;
        path.push_back(g[i][j]), st[i][j] = true;
        dfs(i, j, son[0][t]);
        path.pop_back(), st[i][j] = false;
      }

    for (auto &w : S) res.push_back(w);
    return res;
  }
};