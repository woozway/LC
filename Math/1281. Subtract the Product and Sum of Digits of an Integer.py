class Solution:
  def subtractProductAndSum(self, n: int) -> int:
    return reduce(int.__mul__, map(int, str(n))) - reduce(int.__add__, map(int, str(n)))
