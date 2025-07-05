// 状态表示：f[i]为以s[i]结尾的最长有效括号长度；属性：Max
// 状态计算：当a_i是')'时，按与s[i]匹配的那个'('在哪个位置来进行划分集合
// 如果s[i - 1] == '('，与s[i]的')'匹配，那么：f[i] = f[i - 2] + 2
// 如果s[i - 1] == ')'，那么先找到与s[i - 1]匹配的'('位置：s[i - f[i - 1]]，
// 然后与其上一位置匹配，即：s[i - f[i - 1] - 1] == '('，得出：
// f[i] = f[i - 1] + f[i - f[i - 1] - 2] + 2
const int N = 3e4 + 10;
int f[N];

class Solution {
public:
  int longestValidParentheses(string s) {
    int n = s.size();
    memset(f, 0, sizeof f);

    int res = 0;
    for (int i = 1; i < n; i ++ )
      if (s[i] == ')') {
        if (s[i - 1] == '(') {
          if (i >= 2) f[i] = f[i - 2] + 2;
          else f[i] = 2;
        }
        else if (i - f[i - 1] >= 1 && s[i - f[i - 1] - 1] == '(') {
          if (i - f[i - 1] >= 2) f[i] = f[i - 1] + f[i - f[i - 1] - 2] + 2;
          else f[i] = f[i - 1] + 2;
        }

        res = max(res, f[i]);
      }

    return res;
  }
};