typedef pair<int, int> PII;
const int N = 20 * 20 + 10;
bool st[N]; // 记录是否已在队列中

class Solution {
  int n;

  PII idx2rc(int i) {
    int r = (i - 1) / n, c = (i - 1) % n;
    if (r % 2) c = n - 1 - c;
    return {n - 1 - r, c};
  }

public:
  int snakesAndLadders(vector<vector<int>>& board) {
    n = board.size();
    auto &a = board;

    memset(st, 0, sizeof st);

    queue<PII> q;
    q.push({1, 0});
    st[1] = true;

    while (q.size()) {
      int m = q.size();
      while (m -- ) {
        auto [idx, step] = q.front(); q.pop();
        if (idx == n * n) return step;

        for (int i = idx + 1; i <= min(idx + 6, n * n); i ++ ) {
          auto [r, c] = idx2rc(i);
          int idx_nxt = i;
          if (a[r][c] != -1) idx_nxt = a[r][c];
          if (!st[idx_nxt]) {
            q.push({idx_nxt, step + 1});
            st[idx_nxt] = true;
          }
        }
      }
    }
    return -1;
  }
};