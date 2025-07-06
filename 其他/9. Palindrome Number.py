class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
      return False
    cpx, rev = x, 0
    while cpx:
      rev = rev*10 + cpx%10
      cpx //= 10
    return x == rev
