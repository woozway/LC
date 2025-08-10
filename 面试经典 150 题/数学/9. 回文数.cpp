class Solution {
public:
  bool isPalindrome(int x) {
    if (x < 0) return false;
    if (x < 10) return true;

    string s1 = to_string(x);
    string s2 = s1; reverse(s2.begin(), s2.end());
    
    return s1 == s2;
  }
};