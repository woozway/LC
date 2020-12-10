class Solution:
  def countPrimes(self, n: int) -> int:
    """
    T=O(n), S=O(n), Sieve Of Euler
    """
    primes = []
    isPrime = [1] * n
    for i in range(2, n):
      if isPrime[i]:
        primes.append(i)
      j = 0
      while j < len(primes) and i * primes[j] < n:
        isPrime[i*primes[j]] = 0
        if i % primes[j] == 0:
          break
        j += 1
    return len(primes)
