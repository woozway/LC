// string
// T=O(n)
// S=O(n)

class Solution {
public:
  string replaceSpace(string s) {
    string ret;
    for (auto i : s) {
      if (i == ' ') {
        ret += "%20";
      } else {
        ret += i;
      }
    }
    return ret;
  }
};
