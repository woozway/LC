class Solution:
  def rotatedDigits(self, N: int) -> int:
    A = list(map(int, str(N)))
    memo = {}
    def dp(i, equality_flag, involution_flag):
      if i == len(A): return +(involution_flag)
      if (i, equality_flag, involution_flag) not in memo:
        ans = 0
        for d in range(A[i]+1 if equality_flag else 10):
          if d in {3,4,7}: continue
          ans += dp(i+1, equality_flag and d == A[i], involution_flag or d in {2,5,6,9})
        memo[i, equality_flag, involution_flag] = ans
      return memo[i, equality_flag, involution_flag]
    return dp(0, True, False)
