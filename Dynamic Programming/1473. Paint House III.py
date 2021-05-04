"""
1. Clarification
2. Possible solutions
    - Brute force + Backtracking
    - Dynamic programming
    - Dynamic programming + optimisation
3. Coding
4. Tests
"""


# # T=O(m * 2^n), S=O(1), Time Limit Exceeded
# class Solution:
#     def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
#         if m < 1 or n < 1: return -1
#         minCost = math.inf
#         def backtrack(idx, blockCnt, tmpCost):
#             nonlocal minCost
#             if idx == m:
#                 if blockCnt == target and tmpCost < minCost:
#                     minCost = tmpCost
#                 return
#             if blockCnt > target or tmpCost > minCost:
#                 return
#             if houses[idx] > 0:
#                 if idx == 0 or houses[idx] != houses[idx-1]:
#                     backtrack(idx + 1, blockCnt + 1, tmpCost)
#                 else:
#                     backtrack(idx + 1, blockCnt, tmpCost)
#             else:
#                 for j in range(n):
#                     houses[idx] = j + 1
#                     if idx == 0 or houses[idx] != houses[idx-1]:
#                         backtrack(idx + 1, blockCnt + 1, tmpCost + cost[idx][j])
#                     else:
#                         backtrack(idx + 1, blockCnt, tmpCost + cost[idx][j])
#                     houses[idx] = 0

#         backtrack(0, 0, 0)
#         return -1 if minCost == math.inf else minCost


# T=O(m*n^2*target), S=O(m*n*target)
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        if m < 1 or n < 1: return -1
        houses = [c - 1 for c in houses]
        dp = [[[math.inf] * target for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue
                for k in range(target):
                    for j0 in range(n):
                        if j == j0:
                            if i == 0:
                                if k == 0:
                                    dp[i][j][k] = 0
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                        elif i > 0 and k > 0:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j0][k - 1])
                    if dp[i][j][k] != math.inf and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]
        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == math.inf else ans


# T=O(m*n*target), S=O(m*n*target)
class Entry:
    def __init__(self):
        self.first = math.inf
        self.first_idx = -1
        self.second = math.inf


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        if m < 1 or n < 1: return -1
        houses = [c - 1 for c in houses]
        dp = [[[math.inf] * target for _ in range(n)] for _ in range(m)]
        best = [[Entry() for _ in range(target)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue
                for k in range(target):
                    if i == 0:
                        if k == 0:
                            dp[i][j][k] = 0
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
                        if k > 0:
                            info = best[i - 1][k - 1]
                            dp[i][j][k] = min(dp[i][j][k], (info.second if j == info.first_idx else info.first))
                    if dp[i][j][k] != math.inf and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]
                    info = best[i][k]
                    if dp[i][j][k] < info.first:
                        info.second = info.first
                        info.first = dp[i][j][k]
                        info.first_idx = j
                    elif dp[i][j][k] < info.second:
                        info.second = dp[i][j][k]
        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == math.inf else ans
