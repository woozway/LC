"""
1. Clarification
2. Possible solutions
    - Brute force
    - sieve of Eratosthenes (κόσκινον Ἐρατοσθένους in Greek)
    - Sieve Of Euler
3. Coding
4. Tests
"""


# # T=O(n*sqrt(n)), S=O(1), Time Limit Exceeded
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         ans = 0
#         for i in range(2, n):
#             ans += self.isPrime(i)
#         return ans
#
#     def isPrime(self, x):
#         i = 2
#         while i * i <= x:
#             if x % i == 0:
#                 return False
#             i += 1
#         return True


# T=O(n*lglgn), S=O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        ans, isPrime = 0, [1] * n
        for i in range(2, n):
            if isPrime[i]:
                ans += 1
                if i * i < n:
                    for j in range(i * i, n, i):
                        isPrime[j] = 0
        return ans


# T=O(n), S=O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
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
