// maths
// T=O(lgn)
// S=O(1)

class Solution {
public:
  int countDigitOne(int n) {
    string s = to_string(n);
    int Sum = 0, magnitude = 0;
    for (int i = s.length()-1; i >= 0; i--) {
      string sleft = s.substr(0, i-1-0+1);
      int left;
      if (sleft.empty()) {
        left = 0;
      } else {
        left = stoi(sleft);
      }
      int digit = stoi(s.substr(i, 1));
      string sright = s.substr(i+1);
      int right;
      if (sright.empty()) {
        right = 0;
      } else {
        right = stoi(sright);
      }
      Sum += (left-1-0+1) * 1 * pow(10, magnitude);
      if (digit == 0) {
        Sum += 0;
      } else if (digit == 1) {
        Sum += 1*1*(right+1);
      } else {
        Sum += 1*1*pow(10, magnitude);
      }
      magnitude++;
    }
    return Sum;
  }
};
