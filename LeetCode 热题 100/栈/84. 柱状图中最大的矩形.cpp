const int N = 1e5 + 10;
int stk[N], tt;
int l[N], r[N]; // l[i]和r[i]分别存i左/右边第一个高度<a[i]的元素下标

class Solution {
public:
  int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    auto &a = heights;
    
    // // O(n^2), TLE
    // int res = 0;
    // for (int i = 0; i < n; i ++ ) {
    //   int h = a[i];
    //   for (int j = i; j >= 0; j -- ) {
    //     h = min(h, a[j]);
    //     res = max(res, h * (i - j + 1));
    //   }
    // }

    // 从左到右，左右到左，用单调栈找左/右边最近的第一个比自己小的数
    for (int tt = 0, i = 0; i < n; i ++ ) {
      while (tt && a[stk[tt]] >= a[i]) tt -- ;
      if (tt) l[i] = stk[tt];
      else l[i] = -1;
      stk[ ++ tt] = i;
    }

    for (int tt = 0, i = n - 1; ~i; i -- ) {
      while (tt && a[stk[tt]] >= a[i]) tt -- ;
      if (tt) r[i] = stk[tt];
      else r[i] = n;
      stk[ ++ tt] = i;
    }
    
    int res = 0;
    for (int i = 0; i < n; i ++ ) res = max(res, a[i] * (r[i] - 1 - (l[i] + 1) + 1));
    return res;
  }
};