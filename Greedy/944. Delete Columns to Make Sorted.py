class Solution:
  def minDeletionSize(self, A: List[str]) -> int:
    return sum(1 for s in [list(s) for s in zip(*A)] if sorted(s) != s)
