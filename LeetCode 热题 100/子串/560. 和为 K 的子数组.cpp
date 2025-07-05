const int N = 2e4 + 10;
int a[N], s[N];

class Solution {
public:
  int subarraySum(vector<int>& nums, int k) {
    int n = nums.size();
    for (int i = 1; i <= n; i ++ ) a[i] = nums[i - 1];

    memset(s, 0, sizeof s);
    for (int i = 1; i <= n; i ++ ) s[i] = s[i - 1] + a[i];

    // int res = 0;
    // for (int i = 1; i <= n; i ++ )
    //   for (int j = 1; j <= i; j ++ )
    //     if (s[i] - s[j - 1] == k) res ++ ;
    // return res;

    unordered_map<int, int> M;
    int res = 0;
    M[0] = 1; // 可以i从0开始，因为需要在M中添加：M[0] = 1
    for (int i = 1; i <= n; i ++ ) {
      if (M.count(s[i] - k)) res += M[s[i] - k]; // 同两数之和
      M[s[i]] ++ ;
    }
    return res;
  }
};