class Solution {
public:
  vector<int> twoSum(vector<int>& numbers, int target) {
    int n = numbers.size();
    auto &a = numbers;

    for (int i = 0, j = n - 1; i < n; i ++ ) {
      while (i < j && a[i] + a[j] > target) j -- ;
      if (i < j)
        if (a[i] + a[j] == target)
          return {i + 1, j + 1};
    }
    return {};
  }
};