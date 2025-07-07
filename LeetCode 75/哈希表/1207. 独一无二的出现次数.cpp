class Solution {
public:
  bool uniqueOccurrences(vector<int>& arr) {
    int n = arr.size();
    auto &a = arr;

    unordered_map<int, int> M;
    for (auto x : a) M[x] ++ ;

    unordered_set<int> S;
    for (auto &[_, v] : M) {
      if (S.count(v)) return false;
      S.insert(v);
    }
    return true;
  }
};