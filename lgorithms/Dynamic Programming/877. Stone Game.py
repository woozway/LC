"""
1. Clarification
2. Possible solutions
    - Dynamic programming
    - Maths
3. Coding
4. Tests
"""


# T=O(n^2), S=O(n^2), dp[i][j]: max diff between plays with piles[i..j] inclusive left
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @functools.lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            parity = (j - i - n) % 2
            if parity == 1:
                return max(piles[i] + dp(i+1, j), piles[j] + dp(i, j-1))
            else:
                return min(-piles[i] + dp(i+1, j), -piles[j] + dp(i, j-1))

        return dp(0, n - 1) > 0


# T=O(1), S=O(1)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
