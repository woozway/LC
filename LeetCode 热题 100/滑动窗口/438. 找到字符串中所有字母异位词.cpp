const int N = 128;
int as[N], ap[N]; // as[i]表示s字串中s[i]字符的统计个数，ap对应p串

class Solution {
public:
  vector<int> findAnagrams(string s, string p) {
    int ns = s.size(), np = p.size();

    memset(as, 0, sizeof as), memset(ap, 0, sizeof ap);
    for (auto &c : p) ap[c] ++ ;

    vector<int> res;
    // 双指针j,i分别指向滑动窗口的左和右边界，维护s窗口内各字符的统计数都<=字串p中
    for (int i = 0, j = 0; i < ns; i ++ ) {
      as[s[i]] ++ ; // 新加入的字符会引起统计个数变化
      while (j <= i && as[s[i]] > ap[s[i]]) as[s[j ++ ]] -- ;
      // 如果此时[j,i]窗口的长度等于np，说明找到异位词
      if (i - j + 1 == np) res.push_back(j);
    }
    return res;
  }
};