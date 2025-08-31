class Solution {
  unordered_map<char, char> M = {{')', '('}, {']', '['}, {'}', '{'}};

public:
  bool isValid(string s) {
    stack<char> stk;
    
    // 如果是左括号，入栈；如果是右括号，看栈顶是否匹配
    for (auto c : s)
      if (!M.count(c)) stk.push(c);
      else {
        if (stk.empty() || stk.top() != M[c]) return false;
        stk.pop();
      }

    return stk.empty();
  }
};