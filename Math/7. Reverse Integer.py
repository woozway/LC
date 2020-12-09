class Solution:
  def reverse(self, x: int) -> int:
    ans = str(x) if x > 0 else str(-x) + '-'
    ans = int(ans[::-1])
    return ans if -2**31 <= ans <= 2**31-1 else 0
