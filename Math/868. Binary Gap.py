class Solution:
  def binaryGap(self, n: int) -> int:
    ans, last = 0, None
    for i in range(32):
      if (n >> i) & 1:
        if last is not None:
          ans = max(ans, i - last)
        last = i
    return ans
