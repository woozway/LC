class Solution:
  def maxDepth(self, s: str) -> int:
    cnt = maxcnt = 0
    for ch in s:
      if ch == '(':
        cnt += 1
        maxcnt = max(maxcnt, cnt)
      elif ch == ')':
        cnt -= 1
    return maxcnt
