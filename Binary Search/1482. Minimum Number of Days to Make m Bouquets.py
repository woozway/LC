"""
1. Clarification
2. Possible solutions
    - Brute force
    - Binary Search
3. Coding
4. Tests
"""


# # T=O(n^2 * k), S=O(n), Time Limit Exceeded
# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         n = len(bloomDay)
#         if n < 1 or m < 1 or k < 1 or m * k > n:
#             return -1
#         elements = sorted(list(set(bloomDay)))
#         for e in elements:
#             i, count, lastFailure = 0, 0, 0
#             while i < n:
#                 flag = True
#                 if i + k > n:
#                     break
#                 else:
#                     tmpList = bloomDay[i:i+k]
#                     for j, tmp in enumerate(tmpList):
#                         if tmp > e:
#                             flag = False
#                             lastFailure = i + j
#                 if flag:
#                     i += k
#                     count += 1
#                     if count == m:
#                         return e
#                 else:
#                     i = lastFailure + 1
#         return -1


# T=O(nlgh), S=O(1), h=max(bloomDay)
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < 1 or m < 1 or k < 1 or m * k > n:
            return -1

        def canMake(days: int) -> bool:
            bouquets = flowers = 0
            for i, bloom in enumerate(bloomDay):
                if bloomDay[i] <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        if bouquets == m:
                            break
                        flowers = 0
                else:
                    flowers = 0
            return bouquets == m

        low, high = 1, max(bloomDay)
        while low < high:
            days = (low + high) // 2
            if canMake(days):
                high = days
            else:
                low = days + 1
        return low
