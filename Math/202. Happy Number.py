class Solution:
  def isHappy(self, n: int) -> bool:  
    """
    T=O(lgn), S=O(1)
    """
    def get_next(num):
      total = 0
      while num > 0:
        num, digit = divmod(num, 10)
        total += digit ** 2
      return total

    turtle = n
    hare = get_next(n)
    while hare != 1 and turtle != hare:
      turtle = get_next(turtle)
      hare = get_next(get_next(hare))
    return hare == 1
