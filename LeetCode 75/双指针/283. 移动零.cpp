class Solution {
public:
  void moveZeroes(vector<int>& nums) {
    int n = nums.size();
    auto &a = nums;
    
    // 0~j是已经排好的
    for (int i = 0, j = 0; i < n; i ++ )
      if (a[i] == 0) {
        // j = i + 1; // O(n)
        j = max(j, i + 1); // j不回退，O(n)
        while (j < n && a[j] == 0) j ++ ;
        if (j < n) swap(a[i], a[j]);
      }
  }
};