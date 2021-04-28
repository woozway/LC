"""
1. Clarification
2. Possible solutions
    - Brute force
    - Using Sqrt Function
    - Binary Search
    - Fermat Theorem
3. Coding
4. Tests
"""


# T=O(c), S=O(1)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt = int(c ** 0.5)
        for i in range(sqrt + 1):
            for j in range(sqrt + 1):
                if i * i + j * j == c:
                    return True
        return False


# T=O(c^1/2 * lgc), S=O(1)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt = int(c ** 0.5)
        for a in range(sqrt + 1):
            b = math.sqrt(c - a * a)
            if b == int(b):
                return True
        return False


# T=O(c^1/2 * lgc), S=O(lgc)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt = int(c ** 0.5)
        for a in range(sqrt + 1):
            b = c - a * a
            if self.binary_search(0, b, b):
                return True
        return False

    def binary_search(self, s, e, n):
        if s > e: return False
        mid = (s + e) // 2
        if mid * mid == n:
            return True
        if mid * mid > n:
            return self.binary_search(s, mid - 1, n)
        return self.binary_search(mid + 1, e, n)


# T=O(c^1/2 * lgc), S=O(1)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt = int(c ** 0.5)
        for i in range(2, sqrt + 1):
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c /= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
        return c % 4 != 3
