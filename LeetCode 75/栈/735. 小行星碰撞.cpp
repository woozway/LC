const int N = 1e4 + 10;
int stk[N], tt;

class Solution {
public:
  vector<int> asteroidCollision(vector<int>& asteroids) {
    int n = asteroids.size();
    auto &a = asteroids;

    vector<int> res;
    for (int i = 0; i < n; i ++ ) {
      if (a[i] > 0) stk[ ++ tt] = a[i];
      else {
        if (tt && stk[tt] * a[i] < 0) {
          while (tt && stk[tt] * a[i] < 0 && abs(stk[tt]) < abs(a[i])) tt -- ;
          if (tt) {
            if (stk[tt] * a[i] < 0) {
              if (abs(stk[tt] == abs(a[i]))) tt -- ;
            }
            else stk[ ++ tt] = a[i];
          }
          else stk[ ++ tt] = a[i];
        }
        else stk[ ++ tt] = a[i];
      }
    }

    while (tt) res.push_back(stk[tt -- ]);
    reverse(res.begin(), res.end());
    return res;
  }
};