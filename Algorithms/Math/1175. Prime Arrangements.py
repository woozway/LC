class Solution:
  def numPrimeArrangements(self, n: int) -> int:
    def cntPrimes(n):
      isPrime = [1]*(n+1)
      cnt = 0
      for i in range(2, n+1):
        if isPrime[i]:
          cnt += 1
          if i*i < n+1:
            for j in range(i*i, n+1, i):
              isPrime[j] = 0
      return cnt
    
    def numOfPermu(n):
      return reduce(mul, [i for i in range(1, n+1)], 1)
    
    cnt = cntPrimes(n)
    return numOfPermu(cnt) * numOfPermu(n-cnt) % (10**9+7)
