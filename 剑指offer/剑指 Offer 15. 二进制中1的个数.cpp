// bit manipulation: x & x-1 to get the last 1
// T=O(lgn)
// S=O(1)

class Solution {
public:
  int hammingWeight(uint32_t n) {
    int count = 0;
    while (n) {
      n &= n - 1;
      count++;
    }
    return count;
  }
};
