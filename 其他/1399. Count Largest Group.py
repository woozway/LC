class Solution:
  def countLargestGroup(self, n: int) -> int:
    def getsum(n):
      ans = 0
      while n:
        ans += n % 10
        n //= 10
      return ans
    d = {}
    maxn = -inf
    cnt = 0
    for i in range(1, n+1):
      k = getsum(i)
      d[k] = d.get(k, 0) + 1
      if d[k] > maxn:
        maxn = d[k]
        cnt = 1
      elif d[k] == maxn:
        cnt += 1
    return cnt
