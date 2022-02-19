class Solution:
  def subtractProductAndSum(self, n: int) -> int:
    return reduce(mul, map(int, str(n))) - reduce(add, map(int, str(n)))
