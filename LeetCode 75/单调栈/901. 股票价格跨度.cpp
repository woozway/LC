const int N = 1e5 + 10;
int a[N], i;
int stk[N], tt;

class StockSpanner {
public:
  StockSpanner() {
    i = tt = 0;
  }
  
  int next(int price) {
    a[ ++ i] = price;

    int res = 0;

    while (tt && a[stk[tt]] <= a[i]) tt -- ;
    if (tt) res = i - stk[tt];
    else res = i;

    stk[ ++ tt] = i;

    return res;
  }
};