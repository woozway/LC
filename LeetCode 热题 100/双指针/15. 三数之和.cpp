class Solution {
public:
  vector<vector<int>> threeSum(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;

    sort(a.begin(), a.end()); // 排序，然后找i,j,k

    vector<vector<int>> res;
    for (int i = 0; i < n; i ++ ) {
      if (i && a[i] == a[i - 1]) continue; // a[i]跳过重复数字

      // 双指针j,k相向找符合条件的组合，参考 167. 两数之和II
      for (int j = i + 1, k = n - 1; j < n; j ++ ) {
        while (j < k && a[i] + a[j] + a[k] > 0) k -- ;

        if (j < k && a[i] + a[j] + a[k] == 0) {
          if (j == i + 1 || a[j] != a[j - 1]) // a[j]跳过重复数字
            res.push_back({a[i], a[j], a[k]});
          k -- ;
        }
      }
    }
    return res;
  }
};