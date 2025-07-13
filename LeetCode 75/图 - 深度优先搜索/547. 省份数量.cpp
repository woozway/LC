const int N = 210;
bool st[N];

class Solution {
  int n;
  vector<vector<int>> a;

  void dfs(int u) {
    st[u] = true;

    for (int i = 0; i < n; i ++ ) {
      int j = a[u][i];
      if (j && !st[i]) dfs(i);
    }
  }

public:
  int findCircleNum(vector<vector<int>>& isConnected) {
    n = isConnected.size();
    a = isConnected;

    memset(st, 0, sizeof st);
    int cnt = 0;
    for (int i = 0; i < n; i ++ )
      if (!st[i]) {
        dfs(i);
        cnt ++ ;
      }

    return cnt;
  }
};