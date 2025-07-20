class Solution {
public:
  int minFlips(int a, int b, int c) {
    int res = 0;
    
    for (int i = 30; ~i; i -- )
      if (c >> i & 1) {
        if (!(a >> i & 1) & !(b >> i & 1)) res += 1;
      }
      else {
        if ((a >> i & 1) & (b >> i & 1)) res += 2;
        else if ((a >> i & 1) | (b >> i & 1)) res += 1;
      }

    return res;
  }
};