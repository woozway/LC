typedef pair<int, int> PII;
const int N = 110;
int dist[N][N];

class Solution {
public:
  int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
    int m = maze.size(), n = maze[0].size();
    memset(dist, -1, sizeof dist);

    auto &a = maze; auto &e = entrance;
    int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};

    queue<PII> q;
    q.push({e[0], e[1]});
    dist[e[0]][e[1]] = 0;
    a[e[0]][e[1]] = '+';
    while (q.size()) {
      auto [x, y] = q.front(); q.pop();

      for (int i = 0; i < 4; i ++ ) {
        int u = x + dx[i], v = y + dy[i];
        if (u >= 0 && u < m && v >= 0 && v < n && a[u][v] == '.') {
          if (u == 0 || u == m - 1 || v == 0 || v == n - 1) return dist[x][y] + 1;

          a[u][v] = '+';
          dist[u][v] = dist[x][y] + 1;
          q.push({u, v});
        }
      }
    }
    return -1;
  }
};