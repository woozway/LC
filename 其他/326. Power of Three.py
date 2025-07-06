"""
1. Clarification
2. Possible solutions
    - Brute force
    - Behave good
3. Coding
4. Tests
"""


# T=O(1), S=O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3**19 % n == 0


# T=O(1), S=O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
