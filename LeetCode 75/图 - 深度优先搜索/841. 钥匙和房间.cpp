const int N = 1010;
bool st[N];

class Solution {
  int n;
  vector<vector<int>> a;

  void dfs(int u) {
    st[u] = true;

    int m = a[u].size();
    for (int i = 0; i < m; i ++ ) {
      int j = a[u][i];
      if (!st[j]) dfs(j);
    }
  }

public:
  bool canVisitAllRooms(vector<vector<int>>& rooms) {
    n = rooms.size();
    a = rooms;
    
    memset(st, 0, sizeof st);
    dfs(0);

    for (int i = 0; i < n; i ++ )
      if (!st[i]) return false;
    return true;
  }
};