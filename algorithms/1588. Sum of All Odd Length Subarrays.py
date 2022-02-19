class Solution:
  def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    n = len(arr)
    accsum = [0] * (n+1)
    for i in range(n):
      accsum[i+1] = accsum[i] + arr[i]
    ans = 0
    for i in range(n):
      arrlen = 1
      while i+arrlen <= n:
        ans += accsum[i+arrlen] - accsum[i]
        arrlen += 2
    return ans
