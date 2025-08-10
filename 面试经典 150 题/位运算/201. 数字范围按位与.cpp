class Solution {
public:
  int rangeBitwiseAnd(int left, int right) {
    int shift = 0; // 寻找[left, right]的最长公共前缀
    while (left < right) {
      left >>= 1;
      right >>= 1;
      shift ++ ;
    }
    return left << shift;
  }
};