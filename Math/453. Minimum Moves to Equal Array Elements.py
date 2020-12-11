class Solution:
  def minMoves(self, nums: List[int]) -> int:
    minn = min(nums)
    moves = 0
    for num in nums:
      moves += num - minn
    return moves
