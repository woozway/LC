class Solution:
  def removeOuterParentheses(self, S: str) -> str:
    ans, stack = '', []
    for c in S:
      if c == '(': 
        if stack:
          ans += c
        stack.append('(')
      if c == ')': 
        stack.pop()
        if stack:
          ans += c
    return ans
