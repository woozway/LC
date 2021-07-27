// easy peasy
// T=O(n)
// S=O(n)

class Solution {
public:
  vector<int> printNumbers(int n) {
    vector<int> v;
    string smax;
    for (int i = 0; i < n; i++) {
      smax.push_back('9');
    }
    int maxn = stoi(smax);
    for (int i = 1; i <= maxn; i++) {
      v.push_back(i);
    }
    return v;
  }
};
