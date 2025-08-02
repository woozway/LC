class Solution {
public:
  int removeElement(vector<int>& nums, int val) {
    int n = nums.size();
    auto &a = nums;

    for (int i = 0, j = 0; i < n; i ++ )
      if (a[i] == val) {
        j = max(j, i + 1);
        while (j < n && a[j] == val) j ++ ;
        if (j < n) swap(a[i], a[j]);
      }
    
    int res = -1;
    for (int i = 0; i < n; i ++ )
      if (a[i] != val) res = i;

    return res + 1;
  }
};