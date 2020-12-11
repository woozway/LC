class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    """
    3**19 is the maximun num of power of 3 in integer range
    """
    return n > 0 and 3**19 % n == 0
