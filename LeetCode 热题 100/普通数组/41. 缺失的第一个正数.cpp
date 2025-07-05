const int N = 1e5 + 10;
int a[N];

class Solution {
public:
  int firstMissingPositive(vector<int>& nums) {
    int n = nums.size();
    for (int i = 1; i <= n; i ++ ) a[i] = nums[i - 1];

    // [1,2,3,...]：1位置上放1，2位置上放2，否则交换
    for (int i = 1; i <= n; i ++ )
      while (1 <= a[i] && a[i] <= n && a[i] != a[a[i]])
        swap(a[i], a[a[i]]);

    for (int i = 1; i <= n; i ++ )
      if (a[i] != i) return i;

    return n + 1;
  }
};