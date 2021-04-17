"""
1. Clarification
2. Possible solutions
    - Dynamic programming
    - Sliding window
    - Binary search + HashMap
3. Coding
4. Tests
"""


# T=O(m*n), S=O(m*n), m,n are the len of num1,nums2
# see also leetcode 1035 & 718
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


# T=O((n+m)*min(n,m)), S=O(1)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if nums1[addA + i] == nums2[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        if not nums1 or not nums2: return 0
        n, m = len(nums1), len(nums2)
        ret = 0
        for i in range(n):
            length = min(m, n - i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret


# T=O((n+m)lg(min(n,m))), S=O(n)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(length: int) -> bool:
            hashA = 0
            for i in range(length):
                hashA = (hashA * base + nums1[i]) % mod
            bucketA = {hashA}
            mult = pow(base, length - 1, mod)
            for i in range(length, len(nums1)):
                hashA = ((hashA - nums1[i - length] * mult) * base + nums1[i]) % mod
                bucketA.add(hashA)
            hashB = 0
            for i in range(length):
                hashB = (hashB * base + nums2[i]) % mod
            if hashB in bucketA:
                return True
            for i in range(length, len(nums2)):
                hashB = ((hashB - nums2[i - length] * mult) * base + nums2[i]) % mod
                if hashB in bucketA:
                    return True
            return False

        if not nums1 or not nums2: return 0
        base, mod = 113, 10 ** 9 + 9
        left, right = 0, min(len(nums1), len(nums2))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
