class Solution:
  def balancedStringSplit(self, s: str) -> int:
    cnt = rcnt = lcnt = 0
    for ch in s:
      if ch == 'L': lcnt += 1
      elif ch == 'R': rcnt += 1
      if lcnt == rcnt: cnt += 1
    return cnt
