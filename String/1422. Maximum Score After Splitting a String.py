class Solution:
  def maxScore(self, s: str) -> int:
    onecnt = s.count('1')
    ans = 0
    for ch in s[:-1]:
      onecnt = onecnt-1 if ch == '1' else onecnt+1
      ans = max(ans, onecnt)
    return ans
