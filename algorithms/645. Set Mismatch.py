class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    S = sum(set(nums))
    n = len(nums)
    return [sum(nums) - S, n*(n+1)//2 - S]
