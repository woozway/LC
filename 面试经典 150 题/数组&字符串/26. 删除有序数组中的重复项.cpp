class Solution {
public:
  int removeDuplicates(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    // // c++中的unique函数
    // int j = 0;
    // for (int i = 0; i < n; i ++ )
    //   if (!i || a[i] != a[i - 1])
    //     a[j ++ ] = a[i];
    
    // return j;

    int j = 0;
    for (int i = 0; i < n; i ++ ) {
      while (i && i < n && a[i] == a[i - 1]) i ++ ;
      if (i < n) a[j ++ ] = a[i];
    }
    return j;
  }
};