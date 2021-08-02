// prefix sum, array, dynamic programming
// T=O(n)
// S=O(n)

class Solution {
public:
  vector<int> constructArr(vector<int>& a) {
    int n = a.size();
    vector<int> prefix(n, 1);
    vector<int> suffix(n, 1);
    for (int i = 1; i < n; i++) {
      prefix[i] = prefix[i-1] * a[i-1];
    }
    for (int i = n-2; i > -1; i--) {
      suffix[i] = suffix[i+1] * a[i+1];
    }
    vector<int> ans;
    for (int i = 0; i < n; i++) {
      ans.push_back(prefix[i] * suffix[i]);
    }
    return ans;
  }
};
