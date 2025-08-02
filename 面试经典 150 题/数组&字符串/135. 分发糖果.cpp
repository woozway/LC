typedef pair<int, int> PII;

class Solution {
public:
  int candy(vector<int>& ratings) {
    int n = ratings.size();
    // vector<PII> a;
    // for (int i = 0; i < n; i ++ ) a.push_back({ratings[i], i});
    // sort(a.begin(), a.end());

    // vector<int> b(n);
    // for (int i = 0; i < n; i ++ ) {
    //   auto [v, idx] = a[i];
    //   int l = idx - 1;
    //   if (l < 0) b[idx] = max(b[idx], 1);
    //   else {
    //     if (ratings[idx] > ratings[l]) b[idx] = max(b[idx], b[l] + 1);
    //     else b[idx] = max(b[idx], 1);
    //   }
      
    //   int r = idx + 1;
    //   if (r >= n) b[idx] = max(b[idx], 1);
    //   else {
    //     if (ratings[idx] > ratings[r]) b[idx] = max(b[idx], b[r] + 1);
    //     else b[idx] = max(b[idx], 1);
    //   }
    // }

    // int res = 0;
    // for (int i = 0; i < n; i ++ ) res += b[i];
    // return res;

    vector<int> l(n);
    for (int i = 0; i < n; i ++ )
      if (i && ratings[i] > ratings[i - 1]) l[i] = l[i - 1] + 1;
      else l[i] = 1;
    
    vector<int> r(n);
    for (int i = n - 1; ~i; i -- )
      if (i < n - 1 && ratings[i] > ratings[i + 1]) r[i] = r[i + 1] + 1;
      else r[i] = 1;

    int res = 0;
    for (int i = 0; i < n; i ++ ) res += max(l[i], r[i]);
    return res;
  }
};