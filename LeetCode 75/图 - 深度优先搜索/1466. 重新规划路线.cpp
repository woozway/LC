const int N = 5e4 + 10, M = N * 2;
int h[N], e[M], w[M], ne[M], idx = 1;
bool st[N];

void add(int a, int b, int c) {
  e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx ++ ;
}

class Solution {
  int res = 0;

  void dfs(int u) {
    st[u] = true;

    for (int i = h[u]; i; i = ne[i]) {
      int j = e[i];
      if (!st[j]) {
        res += w[i];
        dfs(j);
      }
    }
  }

public:
  int minReorder(int n, vector<vector<int>>& connections) {
    memset(h, 0, sizeof h); memset(ne, 0, sizeof ne); memset(st, 0, sizeof st); idx = 1;

    for (auto c : connections) {
      int a = c[0], b = c[1];
      add(a, b, 1); add(b, a, 0); // 原始边1，添加的反转边0
    }

    dfs(0);
    return res;
  }
};