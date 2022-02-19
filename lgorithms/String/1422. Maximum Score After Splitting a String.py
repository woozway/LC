class Solution:
  def maxScore(self, s: str) -> int:
    cnt = s.count('1')
    ans = 0
    for ch in s[:-1]:
      cnt = cnt-1 if ch == '1' else cnt+1
      ans = max(ans, cnt)
    return ans
