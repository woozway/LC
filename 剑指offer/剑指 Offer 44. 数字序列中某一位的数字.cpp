// maths
// T=O(lgn)
// S=O(1)

class Solution {
public:
  int findNthDigit(int n) {
    long long base = 9, digit = 1;
    int num = 0;
    while (n > base*digit) {
      n -= base*digit;
      num += base;
      base *= 10;
      digit++;
    }
    num += (n-1)/digit + 1;
    int index = (n-1)%digit + 1;
    while (digit-- > index) {
      num /= 10;
    }
    return num%10;
  }
};
