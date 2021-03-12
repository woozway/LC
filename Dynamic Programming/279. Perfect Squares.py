"""
1. Clarification
2. Possible solutions
     - Brute force + Recursion
     - Dynamic programming
     - Greedy
     - Greedy + bfs
     - Maths
3. Coding
4. Tests
"""


# # Time Limit Exceeded
# class Solution:
#     def numSquares(self, n: int) -> int:
#         def minNumSquares(k):
#             if k in square_nums: return 1
#             min_num = inf
#             for square in square_nums:
#                 if k < square:
#                     break
#                 new_num = minNumSquares(k - square) + 1
#                 min_num = min(min_num, new_num)
#             return min_num

#         if n < 1: return 0
#         square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
#         return minNumSquares(n)


# T=O(n * n^1/2), S=O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 1: return 0
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]


# # T=O(n^h/2), S=O(n^1/2)
# class Solution:
#     def numSquares(self, n: int) -> int:
#         def is_divided_by(n, count):
#             if count == 1: return n in square_nums
#             for k in square_nums:
#                 if is_divided_by(n - k, count - 1):
#                     return True
#             return False

#         if n < 1: return 0
#         square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])
#         for count in range(1, n + 1):
#             if is_divided_by(n, count):
#                 return count


# # T=O(n^h/2), S=O((n^1/2)^h)
# class Solution:
#     def numSquares(self, n: int) -> int:
#         if n < 1: return 0
#         square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
#         level = 0
#         queue = {n}
#         while queue:
#             level += 1
#             next_queue = set()
#             for remainder in queue:
#                 for square_num in square_nums:
#                     if remainder == square_num:
#                         return level
#                     elif remainder < square_num:
#                         break
#                     else:
#                         next_queue.add(remainder - square_num)
#             queue = next_queue
#         return level


# # T=O(n^1/2), S=O(1)
# class Solution:
#     def isSquare(self, n: int) -> bool:
#         sq = int(math.sqrt(n))
#         return sq * sq == n

#     def numSquares(self, n: int) -> int:
#         if n < 1: return 0
#         while (n & 3) == 0:
#             n >>= 2
#         if (n & 7) == 7:
#             return 4
#         if self.isSquare(n):
#             return 1
#         for i in range(1, int(n ** (0.5)) + 1):
#             if self.isSquare(n - i * i):
#                 return 2
#         return 3
