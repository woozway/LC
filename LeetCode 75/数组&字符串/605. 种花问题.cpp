const int N = 2e4 + 10;
int a[N];

class Solution {
public:
  bool canPlaceFlowers(vector<int>& flowerbed, int n) {
    int m = flowerbed.size();
    memset(a, 0, sizeof a);
    
    for (int i = 1; i <= m; i ++ ) a[i] = flowerbed[i - 1];

    int res = 0;
    for (int i = 1; i <= m; i ++ )
      if (!a[i])
        if (!a[i - 1] && !a[i + 1]) {
          a[i] = 1;
          res ++ ;
        }

    return res >= n;
  }
};