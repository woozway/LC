class Solution:
  def countAndSay(self, n: int) -> str:
    if n == 1:
      return '1'
    s = self.countAndSay(n-1)
    i, j = 0, 1
    ans = []
    while j <= len(s):
      if j == len(s):
        ans.extend([str(j-i), s[i]])
      elif s[i] != s[j]:
        ans.extend([str(j-i), s[i]])
        i = j
      j += 1
    return ''.join(ans)
