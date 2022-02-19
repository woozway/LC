class Solution:
  def isMonotonic(self, A: List[int]) -> bool:
    inc, dec = 1, 1
    for i in range(1, len(A)):
      if A[i] < A[i-1]: inc = 0
      if A[i] > A[i-1]: dec = 0
    return True if inc or dec else False
