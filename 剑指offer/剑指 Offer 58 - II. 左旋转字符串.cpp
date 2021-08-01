// array, string
// T=O(n)
// S=O(1)

class Solution {
public:
  string reverseLeftWords(string s, int n) {
    reverse(begin(s), begin(s)+n);
    reverse(begin(s)+n, end(s));
    reverse(begin(s), end(s));
    return s;
  }
};
