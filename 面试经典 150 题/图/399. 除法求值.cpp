typedef pair<bool, double> PBD;
const int N = 50, M = N * 2;
int h[N], e[M], ne[M], idx = 1;
double w[M];
bool st[N];
int m = 1;

void add(int a, int b, double c) {
  e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx ++ ;
}

class Solution {
  unordered_map<string, int> M;

  int get(string &s) {
    if (M.count(s)) return M[s];
    M[s] = m;
    return m ++ ;
  }

  PBD dfs(int u, int v, double p) {
    st[u] = true;
    if (u == v) return {true, p};

    for (int i = h[u]; i; i = ne[i]) {
      int j = e[i];
      if (!st[j]) {
        auto [b, d] = dfs(j, v, p * w[i]);
        if (b) return {true, d};
      }
    }
    return {false, p};
  }

public:
  vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
    memset(h, 0, sizeof h); memset(e, 0, sizeof e); memset(w, 0, sizeof w); memset(ne, 0, sizeof ne);
    idx = 1, m = 1;

    int n = equations.size();
    for (int i = 0; i < n; i ++ ) {
      string s1 = equations[i][0], s2 = equations[i][1];

      int a = get(s1), b = get(s2);
      double c = values[i];

      add(a, b, c), add(b, a, 1 / c);
    }

    vector<double> res;
    int m = queries.size();
    for (int i = 0; i < m; i ++ ) {
      memset(st, 0, sizeof st);

      string s1 = queries[i][0], s2 = queries[i][1];

      if (!M.count(s1) || !M.count(s2)) res.push_back(-1);
      else {
        int a = get(s1), b = get(s2);
        auto [r1, r2] = dfs(a, b, 1.0);
        
        if (r1) res.push_back(r2);
        else res.push_back(-1);
      }
    }
    return res;
  }
};