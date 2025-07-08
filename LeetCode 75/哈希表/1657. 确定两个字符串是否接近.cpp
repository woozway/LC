class Solution {
public:
  bool closeStrings(string word1, string word2) {
    int n1 = word1.size(), n2 = word2.size();
    auto &a = word1, &b = word2;

    if (n1 != n2) return false;

    unordered_map<char, int> M1, M2;
    for (int i = 0; i < n1; i ++ ) M1[a[i]] ++ ;
    for (int i = 0; i < n2; i ++ ) M2[b[i]] ++ ;

    for (auto &[k, v] : M1) if (!M2.count(k)) return false;

    vector<int> t1, t2;
    for (auto &[_, v] : M1) t1.push_back(v);
    for (auto &[_, v] : M2) t2.push_back(v);
    sort(t1.begin(), t1.end());
    sort(t2.begin(), t2.end());
    
    return t1 == t2;
  }
};