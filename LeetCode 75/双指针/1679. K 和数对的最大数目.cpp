class Solution {
public:
  int maxOperations(vector<int>& nums, int k) {
    int n = nums.size();
    auto &a = nums;

    // sort(a.begin(), a.end());
    
    // int res = 0;
    // for (int i = 0, j = n - 1; i < n; i ++ ) {
    //   while (j > i && a[i] + a[j] > k) j -- ;
    //   if (j > i)
    //     if (a[i] + a[j] == k) {
    //       res ++ ;
    //       j -- ;
    //     }
    // }
    // return res;

    unordered_map<int, int> M;
    int res = 0;

    for (int i = 0; i < n; i ++ ) {
      int x = k - a[i];
      if (M.count(x) && M[x]) {
        M[x] -- ;
        res ++ ;
      }
      else M[a[i]] ++ ;
    }

    return res;
  }
};