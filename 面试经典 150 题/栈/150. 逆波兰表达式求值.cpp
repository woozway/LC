class Solution {
public:
  int evalRPN(vector<string>& tokens) {
    int n = tokens.size();
    auto &a = tokens;

    stack<int> stk;
    for (int i = 0; i < n; i ++ )
      if (a[i].size() == 1 && !isdigit(a[i][0])) {
        int d = stk.top(); stk.pop();
        int c = stk.top(); stk.pop();
        int e;
        if (a[i] == "+") e = c + d;
        else if (a[i] == "-") e = c - d;
        else if (a[i] == "*") e = c * d;
        else e = c / d;
        stk.push(e);
      }
      else stk.push(stoi(a[i]));

    return stk.top();
  }
};