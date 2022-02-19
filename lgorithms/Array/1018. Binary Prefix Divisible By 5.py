class Solution:
  def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    ans = []
    acc = 0
    for i in range(len(A)):
      acc = 2*acc + A[i]
      ans.append(False if acc %5 else True)
    return ans
