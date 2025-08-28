const int N = 5010;
int h[N], e[N], ne[N], idx = 1; // 邻接表表示图
int q[N], hh, tt = -1; // 队列，hh/tt表示队列头/尾
int d[N];

void add(int a, int b) {
  e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}

class Solution {
public:
  bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    idx = 1, hh = 0, tt = -1;
    memset(h, 0, sizeof h), memset(d, 0, sizeof d);
    auto &g = prerequisites;
    int m = g.size();

    // 连接图中的有向边（b -> a），并统计a的入度
    for (int i = 0; i < m; i ++ ) {
      int a = g[i][0], b = g[i][1];
      add(b, a);
      d[a] ++ ;
    }

    // 把入度不为0的节点加入队列，为拓扑排序做准备
    for (int i = 0; i < numCourses; i ++ )
      if (!d[i]) q[ ++ tt] = i;

    while (hh <= tt) {
      auto t = q[hh ++ ];
      for (int i = h[t]; i; i = ne[i]) {
        int j = e[i];
        if ( -- d[j] == 0) q[ ++ tt] = j;
      }
    }

    // 若图中无环（即图是DAG），则所有的课程都入队过
    if (tt == numCourses - 1) return true;
    else return false;
  }
};