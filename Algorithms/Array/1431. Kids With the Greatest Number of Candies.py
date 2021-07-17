class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    maxn = max(candies)
    return [x+extraCandies >= maxn for x in candies]
