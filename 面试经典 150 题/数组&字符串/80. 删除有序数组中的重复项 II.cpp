class Solution {
public:
  int removeDuplicates(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    int j = 0;
    for (int i = 0, cnt = 0; i < n; i ++ ) {
      while (i && i < n && a[i] == a[i - 1] && cnt >= 2) i ++ ;
      
      if (i < n) {
        if (!i || a[i] != a[i - 1]) cnt = 1;
        else cnt = 2;

        a[j ++ ] = a[i];
      }
    }
    return j;
  }
};