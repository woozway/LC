class Solution {
  unordered_map<char, char> M = {{')', '('}, {']', '['}, {'}', '{'}};
public:
  bool isValid(string s) {
    stack<char> stk;
    
    for (auto c : s)
      if (!M.count(c)) stk.push(c);
      else {
        if (stk.empty() || stk.top() != M[c]) return false;
        stk.pop();
      }

    return stk.empty();
  }
};