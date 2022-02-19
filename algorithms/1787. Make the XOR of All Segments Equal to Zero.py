"""
1. Clarification
2. Possible solutions
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(2^C * k + n), S=O(2^C + n/k)
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        MAXX = 2 ** 10
        n = len(nums)
        dp = [math.inf] * MAXX
        dp[0] = 0
        for i in range(k):
            count = collections.Counter()
            size = 0
            for j in range(i, n, k):
                count[nums[j]] += 1
                size += 1
            t2min = min(dp)
            g = [t2min] * MAXX
            for mask in range(MAXX):
                for x, countx in count.items():
                    g[mask] = min(g[mask], dp[mask ^ x] - countx)
            dp = [val + size for val in g]
        return dp[0]
