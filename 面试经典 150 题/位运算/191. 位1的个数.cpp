class Solution {
public:
  int hammingWeight(int n) {
    int cnt = 0;
    while (n) n -= n & (-n), cnt ++ ; // lowbit操作
    return cnt;
  }
};