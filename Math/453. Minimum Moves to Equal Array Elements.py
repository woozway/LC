class Solution:
  def minMoves(self, nums: List[int]) -> int:
    moves, minn = 0, inf
    for num in nums:
      minn = min(minn, num)
    for num in nums:
      moves += num - minn
    return moves
