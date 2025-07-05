class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> M;
    for (auto &s : strs) {
      string key = s;
      sort(key.begin(), key.end());
      M[key].push_back(s);
    }
    
    vector<vector<string>> res;
    for (auto &[_, v] : M) res.push_back(v); // 像pair<>或者unordered_map<>可以这样拆解，语法糖
    return res;
  }
};