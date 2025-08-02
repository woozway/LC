const int N = 2e4 + 10;
int a[N], s1[N], s2[N]; // s1, s2分别是从左到右和左右到左的前缀最大值

class Solution {
public:
  int trap(vector<int>& height) {
    int n = height.size();
    for (int i = 1; i <= n; i ++ ) a[i] = height[i - 1];

    memset(s1, 0, sizeof s1), memset(s2, 0, sizeof s2);
    for (int i = 1; i <= n; i ++ ) s1[i] = max(s1[i - 1], a[i]);
    for (int i = n; i; i -- ) s2[i] = max(s2[i + 1], a[i]);

    // 双指针i,j指向两头，谁小移动谁
    int res = 0;
    for (int i = 1, j = n; i <= n; i ++ ) {
      while (i < j && s1[i] > s2[j]) {
        res += s2[j] - a[j];
        j -- ;
      }
      if (i < j) res += s1[i] - a[i];
    }
    return res;
  }
};