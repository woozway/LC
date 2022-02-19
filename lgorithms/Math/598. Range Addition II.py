class Solution:
  def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    return min([m] + [op[0] for op in ops]) * min([n] + [op[1] for op in ops])
