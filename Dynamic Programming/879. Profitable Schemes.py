"""
1. Clarification
2. Possible solutions
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(len(group) * n * minProfit), S=O(n * minProfit)
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        cur = [[0] * (n + 1) for _ in range(minProfit + 1)]
        cur[0][0] = 1
        for p0, g0 in zip(profit, group):
            cur2 = [row[:] for row in cur]
            for p1 in range(minProfit + 1):
                p2 = min(p1 + p0, minProfit)
                for g1 in range(n - g0 + 1):
                    g2 = g1 + g0
                    cur2[p2][g2] += cur[p1][g1]
                    cur2[p2][g2] %= MOD
            cur = cur2
        return sum(cur[-1]) % MOD
