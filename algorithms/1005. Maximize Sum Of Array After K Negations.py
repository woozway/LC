class Solution:
  def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
    A.sort()
    for i in range(len(A)):
      if K == 0 or A[i] >= 0:
        break
      A[i] = -A[i]
      K -= 1
    return sum(A) if K == 0 or K % 2 == 0 else sum(A) - 2 * min(A)
