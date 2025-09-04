class Solution {
public:
  void sortColors(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    // 荷兰旗问题：有 p0 个 0，有 p1 - p0 个 1，有 i+1 - p1 个 2
    int p0 = 0, p1 = 0;
    for (int i = 0; i < n; i ++ ) {
      int x = a[i];
      a[i] = 2;
      if (x <= 1) a[p1 ++ ] = 1;
      if (x == 0) a[p0 ++ ] = 0;
    }
  }
};