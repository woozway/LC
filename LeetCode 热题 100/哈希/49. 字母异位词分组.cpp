class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    // 每个s排序后放到同类vector中即可
    unordered_map<string, vector<string>> M;
    for (auto &s : strs) {
      string key = s;
      sort(key.begin(), key.end());
      M[key].push_back(s);
    }
    
    vector<vector<string>> res;
    // 像pair或unordered_map可这样拆解，语法糖
    for (auto &[_, v] : M) res.push_back(v);
    return res;
  }
};