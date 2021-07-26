// T=O(n)
// S=O(n), can be optimised to be O(1)

class Solution {
public:
  int fib(int n) {
    vector<int> v;
    v.push_back(0);
    v.push_back(1);
    for (int i = 2; i < n+1; i++) {
      v.push_back((v[i-2] + v[i-1]) % 1000000007);
    }
    return v[n];
  }
};
