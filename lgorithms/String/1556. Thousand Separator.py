class Solution:
  def thousandSeparator(self, n: int) -> str:
    """
    T=O(lgn), S=O(lgn)
    """
    cnt = 0
    ans = []
    while True:
      cur = n % 10
      n //= 10
      ans.append(str(cur))
      cnt += 1
      if cnt % 3 == 0 and n > 0:
        ans.append('.')
      if n == 0:
        break
    return ''.join(ans[::-1])
