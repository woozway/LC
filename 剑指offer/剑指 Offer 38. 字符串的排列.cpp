// backtracking, recursion
// T=O(n*n!)
// S=O(n)

class Solution {
public:
  vector<string> permutation(string s) {
    vector<string> v;
    if (s.size() <= 1) {
      v.push_back(s);
      return v;
    }
    for (int i = 0; i < s.size(); i++) {
      swap(s[0], s[i]);
      vector<string> ret = permutation(s.substr(1));
      for (auto x : ret) {
        v.push_back(s[0] + x);
      }
      swap(s[0], s[i]);
    }
    unordered_set<string> us;
    vector<string> ans;
    for (int i = 0; i < v.size(); i++) {
      if (us.find(v[i]) == us.end()) {
        us.insert(v[i]);
        ans.push_back(v[i]);
      }
    }
    return ans;
  }
};
