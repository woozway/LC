"""
1. Clarification
2. Possible solutions
    - Dynamic programming v1
    - Dynamic programming v2
3. Coding
4. Tests
"""


# T=O(lmn + L), S=O(lmn)
# dp[i][j][k]: max # of strings with 0 j times and 1 k times for previous i strings
class Solution:
    def getZerosOnes(self, s):
        zerosOnes = [0] * 2
        for ch in s:
            zerosOnes[ord(ch) - ord('0')] += 1
        return zerosOnes

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        len_ = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len_ + 1)]
        for i in range(1, len_ + 1):
            zerosOnes = self.getZerosOnes(strs[i - 1])
            zeros, ones = zerosOnes[0], zerosOnes[1]
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-zeros][k-ones] + 1)
        return dp[len_][m][n]


# T=O(lmn + L), S=O(mn)
class Solution:
    def getZerosOnes(self, s):
        zerosOnes = [0] * 2
        for ch in s:
            zerosOnes[ord(ch) - ord('0')] += 1
        return zerosOnes

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        len_ = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(len_):
            zerosOnes = self.getZerosOnes(strs[i])
            zeros, ones = zerosOnes[0], zerosOnes[1]
            for j in range(m, zeros - 1, -1):
                for k in range(n, ones - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1)
        return dp[m][n]
