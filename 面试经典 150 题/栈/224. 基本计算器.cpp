class Solution {
  stack<int> num;
  stack<char> op;

  void eval() {
    auto b = num.top(); num.pop();
    auto a = num.top(); num.pop();
    auto o = op.top(); op.pop();

    int x;
    if (o == '+') x = a + b;
    else if (o == '-') x = a - b;
    num.push(x);
  }

public:
  int calculate(string s) {
    string str;
    for (int i = 0; i < s.size(); i ++ ) if (!isspace(s[i])) str += s[i];

    unordered_map<char, int> pr{{'+', 1}, {'-', 1}, {'*', 2}, {'/', 2}};

    for (int i = 0; i < str.size(); i ++ ) {
      auto c = str[i];
      if (isdigit(c) || (c == '-' && (!i || str[i - 1] == '('))) {
        int sign = 1;
        if (c == '-') {
          sign = -1, i ++ ;
          if (!isdigit(str[i])) op.push(c);
        }
        int x = 0, j = i;
        while (j < str.size() && isdigit(str[j])) x = x * 10 + (str[j ++ ] - '0');
        num.push(sign * x);
        i = j - 1;
      }
      else if (c == '(') op.push(c);
      else if (c == ')') {
        while (op.top() != '(') eval();
        op.pop();
      }
      else {
        while (op.size() && op.top() != '(' && pr[op.top()] >= pr[c]) eval();
        op.push(c);
      }
    }

    while (op.size()) eval();
    return num.top();
  }
};