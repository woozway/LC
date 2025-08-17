class Solution {
  string sa, sb, sc;
  int n1, n2, n3;
  unordered_map<int, bool> M;

  int get(int i, int j, int k) {
    return i * 100 + j * 10 + k;
  }

  bool dfs(int i, int j, int k) {
    int key = get(i, j, k);
    if (M.count(key)) return M[key];

    if (i >= n1) return M[key] = (sb.substr(j) == sc.substr(k));
    if (j >= n2) return M[key] = (sa.substr(i) == sc.substr(k));
    if (k >= n3) return M[key] = true;

    if (sc[k] == sa[i])
      if (dfs(i + 1, j, k + 1)) return M[key] = true;

    if (sc[k] == sb[j])
      if (dfs(i, j + 1, k + 1)) return M[key] = true;

    return M[key] = false;
  }
  
public:
  bool isInterleave(string s1, string s2, string s3) {
    if (s1.size() + s2.size() != s3.size()) return false;

    sa = s1, sb = s2, sc = s3;
    n1 = s1.size(), n2 = s2.size(), n3 = s3.size();
    
    return dfs(0, 0, 0);
  }
};