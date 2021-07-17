"""
1. Clarification
2. Possible solutions
    - Python built-in
    - Python library function
    - binary search
    - Newton's method
3. Coding
4. Tests
"""


# T=O(lgn), S=O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num ** 0.5 % 1 == 0


# T=O(lgn), S=O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1: return False
        if num == 1: return True
        sqr = int(math.sqrt(num))
        return sqr * sqr == num


# T=O(lgn), S=O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1: return False
        if num == 1: return True
        left, right = 2, num // 2
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        return False


# T=O(lgn), S=O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1: return False
        if num == 1: return True
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num
