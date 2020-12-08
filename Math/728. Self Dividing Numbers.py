class Solution:
  def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    def self_dividing(n):
      for d in str(n):
        if d == '0' or n % int(d) > 0:
          return False
      return True
    return list(filter(self_dividing, range(left, right+1)))
