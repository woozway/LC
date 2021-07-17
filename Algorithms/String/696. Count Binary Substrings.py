class Solution:
  def countBinarySubstrings(self, s: str) -> int:
    n = len(s)
    i = last = ans = 0
    while i < n:
      c = s[i]
      cnt = 0
      while i < n and s[i] == c:
        i += 1
        cnt += 1
      ans += min(cnt, last)
      last = cnt
    return ans
