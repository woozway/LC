const int N = 1010;
bool st[N]; // st[i]记录i在堆中

class SmallestInfiniteSet {
  priority_queue<int, vector<int>, greater<int>> q;
  int idx = 1; // >= idx 是都还没弹出堆的正整数

public:
  SmallestInfiniteSet() {
    memset(st, 0, sizeof st);
  }
  
  int popSmallest() {
    int res = -1;
    if (!q.size())
      res = idx ++ ;
    else {
      res = q.top(); q.pop();
      st[res] = false;
    }
    return res;
  }
  
  void addBack(int num) {
    if (st[num]) return;
    if (num >= idx) return;

    if (num == idx - 1) idx -- ;
    else {
      q.push(num);
      st[num] = true;
    }
  }
};