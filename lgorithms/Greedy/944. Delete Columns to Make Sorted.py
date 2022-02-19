class Solution:
  def minDeletionSize(self, A: List[str]) -> int:
    return sum(1 for col in zip(*A) if any(col[i] > col[i+1] for i in range(len(col) - 1)))
