class Solution:
  def romanToInt(self, s: str) -> int:
    a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}        
    ans, n = 0, len(s)
    for i in range(n):
      if i < n-1 and a[s[i]] < a[s[i+1]]:
        ans -= a[s[i]]
      else:
        ans += a[s[i]]
    return ans
