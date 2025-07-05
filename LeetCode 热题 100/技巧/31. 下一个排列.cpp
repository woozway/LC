class Solution {
public:
  void nextPermutation(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    int i = n - 2; // 找第一个i满足a[i] < a[i+1]
    while (i >= 0 && a[i] >= a[i + 1]) i -- ;

    if (i >= 0) {
      int j = n - 1; // 找i右侧右向左第一个j满足a[i] < a[j]
      while (a[j] <= a[i]) j -- ;
      swap(a[i], a[j]); // 交换后i右边的序列仍是递减的
    }

    reverse(a.begin() + i + 1, a.end()); // 排序i右边的序列
  }
};