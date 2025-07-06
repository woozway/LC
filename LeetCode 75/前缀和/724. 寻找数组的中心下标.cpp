const int N = 1e4 + 10;
int s1[N], s2[N]; // s1和s2分别左往右和右往左的前缀和
int a[N];

class Solution {
public:
  int pivotIndex(vector<int>& nums) {
    int n = nums.size();
    for (int i = 1; i <= n; i ++ ) a[i] = nums[i - 1];

    memset(s1, 0, sizeof s1);
    memset(s2, 0, sizeof s2);
    for (int i = 1; i <= n; i ++ ) s1[i] = s1[i - 1] + a[i];
    for (int i = n; i >= 1; i -- ) s2[i] = s2[i + 1] + a[i];

    for (int i = 1; i <= n; i ++ )
      if (s1[i - 1] == s2[i + 1]) return i - 1;
    return -1;
  }
};