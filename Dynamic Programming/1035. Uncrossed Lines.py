"""
1. Clarification
2. Possible solutions
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(m*n), S=O(m*n), m,n are the len of A,B
# dp[i][j]: Longest Common Sequence ends with A[i] and B[j], index starts from 1
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if not A or not B: return 0
        m, n = len(A), len(B)
        ans = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return ans
