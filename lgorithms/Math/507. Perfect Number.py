class Solution:
  def checkPerfectNumber(self, num: int) -> bool:
    """
    T=O(1), S=O(1), p in Mersenne number
    """
    def pn(p):
      return (1 << (p - 1)) * ((1 << p) - 1)

    primes = [2,3,5,7,13,17,19,31]
    for prime in primes:
      if pn(prime) == num:
        return True
    return False
