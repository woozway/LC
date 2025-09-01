const int N = 1e5 + 10;
int h[N], cnt;

void down(int u) {
  int t = u;
  if (u * 2 <= cnt && h[t] < h[u * 2]) t = u * 2;
  if (u * 2 + 1 <= cnt && h[t] < h[u * 2 + 1]) t = u * 2 + 1;
  if (t != u) {
    swap(h[t], h[u]);
    down(t);
  }
}

class Solution {
public:
  int findKthLargest(vector<int>& nums, int k) {
    int n = nums.size();
    for (int i = 1; i <= n; i ++ ) h[i] = nums[i - 1];
    cnt = n;

    // O(n)建堆
    for (int i = n / 2; i; i -- ) down(i);

    int res;
    while (k -- ) {
      res = h[1];
      swap(h[1], h[cnt -- ]);
      down(1);
    }
    return res;
  }
};