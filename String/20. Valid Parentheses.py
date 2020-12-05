class Solution:
  def isValid(self, s: str) -> bool:
    d = {'{':'}', '[':']', '(':')', '?':'?'}
    stack = ['?']
    for ch in s:
      if ch in d:
        stack.append(ch)
      elif d[stack.pop()] != ch:
        return False 
    return len(stack) == 1
