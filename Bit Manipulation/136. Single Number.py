class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    """ a ^ 0 = a, a ^ a = 0, 
        a ^ b ^ a = b ^ a ^ a = b ^ (a ^ a) = b ^ 0 = b
    """
    return reduce(lambda x, y: x ^ y, nums)
