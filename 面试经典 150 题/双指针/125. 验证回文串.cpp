class Solution {
public:
  bool isPalindrome(string s) {
    int n = s.size();

    for (int i = 0, j = n - 1; i < n; i ++ )
      if (isalnum(s[i])) {
        while (i < j && !isalnum(s[j])) j -- ;
        if (i < j)
          if (tolower(s[i]) != tolower(s[j -- ]))
            return false;
      }

    return true;
  }
};