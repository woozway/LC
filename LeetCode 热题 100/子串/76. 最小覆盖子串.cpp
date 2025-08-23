const int N = 1e5 + 10;
int as[N], at[N]; // as[i]表示s字串中s[i]字符的统计个数，at对应t串

class Solution {
public:
  string minWindow(string s, string t) {
    int ns = s.size(), nt = t.size();
    memset(as, 0, sizeof as), memset(at, 0, sizeof at);

    // for (auto &c : t) at[c] ++ ;

    // int len = 1e9, st = -1;
    // for (int i = 0, j = 0; i < ns; i ++ ) {
    //   as[s[i]] ++ ;
    //   while (j <= i && as[s[j]] > at[s[j]]) as[s[j ++ ]] -- ;

    //   if (i - j + 1 >= len) continue;

    //   bool flag = true;
    //   for (int k = 0; k < nt; k ++ )
    //     if (as[t[k]] < at[t[k]])
    //       flag = false;

    //   if (flag) {
    //     len = i - j + 1;
    //     st = j;
    //   }
    // }

    int cnt = 0; // 记录t中不重复的字符个数，同时动态记录t中尚未被覆盖的字符个数
    for (auto &c : t) if (!at[c] ++ ) cnt ++ ;

    int len = 1e9, st = -1;
    // 双指针j,i分别指向滑动窗口的左和右边界，保持s窗口内的各字符统计数都<=字串t中
    for (int i = 0, j = 0; i < ns; i ++ ) {
      if (++ as[s[i]] == at[s[i]]) cnt -- ;

      while (j <= i && as[s[j]] > at[s[j]]) -- as[s[j ++ ]];

      if (j <= i && cnt == 0) // 窗口中覆盖t中全部字符
        if (len > i - j + 1) {
          len = i - j + 1;
          st = j;
        }
    }

    if (len == 1e9) return "";
    return s.substr(st, len);
  }
};