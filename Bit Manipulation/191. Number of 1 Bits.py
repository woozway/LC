class Solution:
  def hammingWeight(self, n: int) -> int:
    """ Brian Kernighan Algorithm """
    cnt = 0
    while n:
      n &= n-1
      cnt += 1
    return cnt
