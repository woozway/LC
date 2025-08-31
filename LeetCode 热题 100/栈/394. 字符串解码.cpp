class Solution {
public:
  string decodeString(string s) {
    int n = s.size();
    stack<string> stk1;
    stack<int> stk2;

    for (int i = 0; i < n; i ++ )
      if (s[i] == ']') {
        string str = "";
        while (stk1.top() != "[") str = stk1.top() + str, stk1.pop();
        stk1.pop();

        int m = stk2.top(); stk2.pop();
        string t = "";
        while (m -- ) t += str;
        stk1.push(t);
      }
      else if (isdigit(s[i])) {
        int j = i, x = 0;
        while (j < n && isdigit(s[j])) x = x * 10 + s[j ++ ] - '0';

        stk2.push(x);
        i = j - 1;
      }
      else stk1.push(string(1, s[i]));

    string res = "";
    while (stk1.size()) res = stk1.top() + res, stk1.pop();
    return res;
  }
};