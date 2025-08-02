const int N = 5010;
int a[N], b[N];

void insert(int l, int r, int c) {
  b[l] += c, b[r + 1] -= c;
}

class Solution {
public:
  int hIndex(vector<int>& citations) {
    int n = citations.size();
    for (int i = 1; i <= n; i ++ ) a[i] = citations[i - 1];

    memset(b, 0, sizeof b);
    for (int i = 1; i <= n; i ++ ) insert(0, a[i], 1);

    for (int i = 1; i <= n; i ++ ) b[i] += b[i - 1];

    // 找到最后一个b[i]>=i的
    int l = 0, r = n;
    while (l < r) {
      int mid = l + r + 1 >> 1;
      if (b[mid] >= mid) l = mid;
      else r = mid - 1;
    }
    return l;
  }
};