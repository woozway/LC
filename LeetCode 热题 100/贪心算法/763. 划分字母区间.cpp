class Solution {
public:
  vector<int> partitionLabels(string s) {
    int n = s.size();

    unordered_map<char, int> M;
    for (int i = 0; i < n; i ++ ) M[s[i]] = i;

    vector<int> res;
    int ed = -1;
    for (int i = 0; i < n; i ++ ) {
      ed = max(ed, M[s[i]]);
      if (i == ed) {
        ed = -1;
        res.push_back(i + 1);
      }
    }

    n = res.size();
    for (int i = n - 1; i > 0; i -- ) res[i] -= res[i - 1];
    return res;
  }
};