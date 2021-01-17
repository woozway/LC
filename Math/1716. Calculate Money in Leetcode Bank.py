"""
1. Clarification
2. Possible solutions
 - simulation
 - math
3. Coding
4. Tests
"""

# T=O(n), S=O(n)
class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(i%7 + 1 + i//7 for i in range(n))

# # T=O(1), S=O(1)
# class Solution:
#     def totalMoney(self, n: int) -> int:
#         fullWeek, day = n // 7, n % 7
#         return (49 + 7*fullWeek) * fullWeek // 2 + (2*fullWeek + day + 1) * day // 2
