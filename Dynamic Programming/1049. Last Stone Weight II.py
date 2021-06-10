"""
1. Clarification
2. Possible solutions
    - Dynamic programming v1
    - Dynamic programming v2
3. Coding
4. Tests
"""


# T=O(n*sum), S=O(m*n)
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(n):
            for j in range(m + 1):
                if j < stones[i]:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j] or dp[i][j - stones[i]]
        ans = None
        for j in range(m, -1, -1):
            if dp[n][j]:
                ans = total - 2 * j
                break
        return ans


# T=O(n*sum), S=O(sum)
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [False] * (m + 1)
        dp[0] = True
        for weight in stones:
            for j in range(m, weight - 1, -1):
                dp[j] |= dp[j - weight]
        ans = None
        for j in range(m, -1, -1):
            if dp[j]:
                ans = total - 2 * j
                break
        return ans
