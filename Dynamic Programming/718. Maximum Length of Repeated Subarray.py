"""
1. Clarification
2. Possible solutions
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(m*n), S=O(m*n), m,n are the len of num1,nums2
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2: return 0
        m, n = len(nums1), len(nums2)
        ans = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans
