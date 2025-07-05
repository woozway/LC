const int N = 1e5 + 10;
int h[N], cnt;

class Solution {
  unordered_map<int, int> M;

  void down(int u) {
    int t = u;
    if (u * 2 <= cnt && M[h[t]] < M[h[u * 2]]) t = u * 2;
    if (u * 2 + 1 <= cnt && M[h[t]] < M[h[u * 2 + 1]]) t = u * 2 + 1;
    if (t != u) {
      swap(h[t], h[u]);
      down(t);
    }
  }

public:
  vector<int> topKFrequent(vector<int>& nums, int k) {
    int n = nums.size();
    auto &a = nums;
    
    for (auto x : a) M[x] ++ ;
    int i = 1;
    for (auto [key, val] : M) h[i ++ ] = key;
    cnt = M.size();
    
    for (int i = cnt / 2; i; i -- ) down(i);

    vector<int> res;
    while (k -- ) {
      res.push_back(h[1]);
      swap(h[1], h[cnt -- ]);
      down(1);
    }
    return res;
  }
};