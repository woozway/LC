class Solution:
  def isHappy(self, n: int) -> bool:  
    """
    T=O(lgn), S=O(1), Floyd's cycle detection algo
    """
    def get_next(num):
      total = 0
      while num > 0:
        num, digit = divmod(num, 10)
        total += digit ** 2
      return total

    tortoise = n
    hare = get_next(n)
    while hare != 1 and tortoise != hare:
      tortoise = get_next(tortoise)
      hare = get_next(get_next(hare))
    return hare == 1
