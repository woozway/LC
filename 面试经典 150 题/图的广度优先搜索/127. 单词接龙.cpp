const int N = 5010 * 10, M = N * 2;
int h[N], e[M], ne[M], idx = 1;
int dist[N];
int m = 1;

void add(int a, int b) {
  e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}

class Solution {
  unordered_map<string, int> M;

  int get(string &s) {
    if (M.count(s)) return M[s];
    M[s] = m;
    return m ++ ;
  }

  void add_edge(string &w) {
    int a = get(w);
    for (char &ch : w) {
      char t = ch;
      ch = '*';
      int b = get(w);
      add(a, b), add(b, a);
      ch = t;
    }
  }

public:
  int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    memset(h, 0, sizeof h), memset(e, 0, sizeof e), memset(ne, 0, sizeof ne), memset(dist, 0x3f, sizeof dist);
    idx = 1, m = 1;

    for (string &w : wordList) add_edge(w);
    if (!M.count(endWord)) return 0;

    add_edge(beginWord);

    int bid = M[beginWord], eid = M[endWord];
    dist[bid] = 0;
    queue<int> q;
    q.push(bid);
    while (q.size()) {
      auto u = q.front(); q.pop();
      if (u == eid) return dist[eid] / 2 + 1;

      for (int i = h[u]; i; i = ne[i]) {
        int j = e[i];
        if (dist[j] == 0x3f3f3f3f) {
          dist[j] = dist[u] + 1;
          q.push(j);
        }
      }
    }
    return 0;
  }
};