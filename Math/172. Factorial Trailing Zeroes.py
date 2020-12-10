class Solution:
  def trailingZeroes(self, n: int) -> int:
    """
    T=O(lgn), S=O(1)
    """
    zero_count = 0
    while n > 0:
      n //= 5
      zero_count += n
    return zero_count
