const int N = 128;
int a[N];

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int n = s.size();

    memset(a, 0, sizeof a);
    int res = 0;
    // 双指针j,i分别指向滑动窗口的左和右边界
    for (int i = 0, j = 0; i < n; i ++ ) {
      a[s[i]] ++ ; // 新加入的字符会引起统计个数变化
      // 维护窗口内元素个数都<=1，写j<n也可以
      while (j <= i && a[s[i]] > 1) a[s[j ++ ]] -- ;
      res = max(res, i - j + 1);
    }
    return res;
  }
};