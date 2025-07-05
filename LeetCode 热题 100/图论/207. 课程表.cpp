const int N = 5010;
int h[N], e[N], ne[N], idx = 1;
int q[N], hh, tt = -1;
int d[N];

void add(int a, int b) {
  e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}

class Solution {
public:
  bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    idx = 1, hh = 0, tt = -1;
    memset(h, 0, sizeof h), memset(d, 0, sizeof d);
    auto &g = prerequisites;
    int m = g.size();

    for (int i = 0; i < m; i ++ ) {
      int a = g[i][0], b = g[i][1];
      add(b, a);
      d[a] ++ ;
    }

    for (int i = 0; i < numCourses; i ++ )
      if (!d[i]) q[ ++ tt] = i;

    while (hh <= tt) {
      auto t = q[hh ++ ];
      for (int i = h[t]; i; i = ne[i]) {
        int j = e[i];
        if ( -- d[j] == 0) q[ ++ tt] = j;
      }
    }

    if (tt == numCourses - 1) return true;
    else return false;
  }
};