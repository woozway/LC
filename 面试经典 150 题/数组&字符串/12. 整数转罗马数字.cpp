string R[4][10] = {
  {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}, // 个位
  {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}, // 十位
  {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}, // 百位
  {"", "M", "MM", "MMM"}, // 千位
};

class Solution {
public:
  string intToRoman(int num) {
    auto a = num;
    return R[3][a / 1000] + R[2][a / 100 % 10] + R[1][a / 10 % 10] + R[0][a % 10];
  }
};